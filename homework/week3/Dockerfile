FROM ubuntu:latest
RUN apt update

FROM python:3
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy matplotlib pandas
    # Note: we had to merge the two "pip install" package lists here, otherwise
    # the last "pip install" command in the OP may break dependency resolution…

#FROM python: 3.10
WORKDIR /usr/app/src.
COPY first_plot.py ./
COPY coding-environment-exercise.csv ./
CMD ["python","first_plot.py"]
EXPOSE 8080

#we should remember that docker should have the libraries needed