import os
import psycopg2
"postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"
#Database initialization
SQLALCHEMY_DATABASE_URI = "postgresql://lpckxwbwjcxhfj:2310c4b0a50aee21c04b277dc4deb6789d46ca592f0a596b6bf51c911c860249@ec2-63-34-223-144.eu-west-1.compute.amazonaws.com:5432/ddm7ptlanc8iau"
# psycopg2.connect(
#     dbname="ddm7ptlanc8iau",
#     user="lpckxwbwjcxhfj",
#     password="2310c4b0a50aee21c04b277dc4deb6789d46ca592f0a596b6bf51c911c860249",
#     host="ec2-63-34-223-144.eu-west-1.compute.amazonaws.com",
#     port="5432")


SECRET_KEY = 'VerySecret'
SQLALCHEMY_TRACK_MODIFICATIONS = False


