#!/bin/bash
echo **********************************************************
echo Starting the replica set
echo **********************************************************

sleep 10 | echo Sleeping

mongosh mongo-rs0-1:30001 replicaSet.js