import json
import sys

'''Read file and convert Json to Dict'''
def read_input(input_file):
    with open(input_file) as f:
        data = json.loads(f.read())
        return data


def get_output(data):

    ro = data['data']

    c_t = []
    g_t = []

    '''
    1.Does not append to list if atleast one of attributes is None.
    2.Create separate list for corporate and government bond.
    '''
    for i in ro:
        type = i['id'][0]
        if type == 'c':
            id = i['id']
            type = i['type']
            tenor = i['tenor']
            yield_value = i['yield']
            amount_outstanding = i['amount_outstanding']
            if all(c is not None for c in [id, type, tenor, yield_value, amount_outstanding]):
                c_t.append(i)
        else:
            id = i['id']
            type = i['type']
            tenor = i['tenor']
            yield_value = i['yield']
            amount_outstanding = i['amount_outstanding']
            if all(g is not None for g in [id, type, tenor, yield_value, amount_outstanding]):
                g_t.append(i)

    '''
    Sort by outstanding amount for govt bond.This will help to choose the bond with hightest outstanding amount in case of equal tenor.
    '''
    g_sorted = sorted(g_t, key=lambda i: i['amount_outstanding'], reverse=True)

    for c in c_t:
        c_id = c['id'].strip()
        c_tenor = c['tenor'].replace("years","").strip()
        c_yield = c['yield'].replace("%", "").strip()
        c_ao = c['amount_outstanding']
        temp_tenor = 99999
        temp_os = 0
        g_type = ""
        for g in g_sorted:
            g_id = g['id'].strip()
            g_tenor = g['tenor'].replace("years", "").strip()
            g_yield = g['yield'].replace("%", "").strip()
            g_ao = g['amount_outstanding']
            calc_tenor = abs(float(c_tenor) - float(g_tenor))
            if calc_tenor < temp_tenor:
                temp_tenor = calc_tenor
                calc_yield = abs(float(c_yield) - float(g_yield))
                g_type = g_id

            bps = round(calc_yield,2) * 100
            bps_fmt = str(bps) + " bps"

        new_dict = {"corporate_bond_id": c_id, "government_bond_id" : g_type, "spread_to_benchmark" : bps_fmt }
        return new_dict

'''Convert Dict to JSON and write file'''
def write_output(dict,output_file):
    with open(output_file, 'w') as outfile:
        json.dump(dict, outfile,indent=2)




def main():
    if len(sys.argv) == 3:
        input_file = sys.argv[1] #input_file.json
        output_file = sys.argv[2] #output_file.json
        data = read_input(input_file)
        output = get_output(data)
        write_output(output,output_file)
    else:
        raise ('2 parameters required,For input file and output file')

if __name__ == "__main__":
    main()

