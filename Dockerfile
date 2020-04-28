FROM python:3
COPY sde-test-solution.py /
COPY input_file.json ./
COPY output_file.json ./
ENTRYPOINT ["python","sde-test-solution.py"]
CMD ["input_file.json","output_file.json"]
