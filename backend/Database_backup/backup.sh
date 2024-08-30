#!/bin/bash

# Run the pg_dump command
pg_dump -h localhost -U kubiu_user -d kubiu_outfitters_db -F c -b -v -f Kubiu_outfitters_db.backup

# Check if the command was successful
if [ $? -eq 0 ]; then
  echo "Backup completed successfully!"
else
  echo "Backup failed with error code $?"
fi
