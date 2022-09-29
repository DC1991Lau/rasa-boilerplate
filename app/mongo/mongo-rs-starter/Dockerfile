FROM bitnami/mongodb

# Create app directory
WORKDIR /mongo

# Install app dependencies
COPY replicaSet.js .
COPY setup.sh .

# RUN chmod +x setup.sh

CMD ["./setup.sh"]