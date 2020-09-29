FROM python
RUN pip install pyyaml
COPY . .
CMD python gen-pipelines.py
