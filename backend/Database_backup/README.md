# If you are reading this you are f*cked
# PostgreSQL Backup and Restore Guide

This guide provides instructions on how to create a backup of your PostgreSQL database and restore it from a backup. Follow these steps to ensure that you have a reliable backup and can recover your database in case of any issues.

## 1. Creating a Backup

To create a backup of your PostgreSQL database, use the `pg_dump` command. Follow these steps:

1. **Open a Terminal**: Access your terminal or command line interface.

2. **Run the Backup Command**: Use the following command to create a backup of your database:

   ```bash
   pg_dump -h localhost -U kubiu_user -d kubiu_outfitters_db -F c -b -v -f backup_filename.backup
   ```

   ### Command Explanation:

   - `pg_dump`: The PostgreSQL utility used to create a backup of your database.
   - `-h localhost`: Specifies the host where your PostgreSQL server is running. `localhost` refers to your local machine.
   - `-U kubiu_user`: Specifies the PostgreSQL user to connect as. Replace `kubiu_user` with your actual username.
   - `-d kubiu_outfitters_db`: Specifies the name of the database you want to back up.
   - `-F c`: Specifies the format of the backup file. `c` stands for custom format, which is compressed and allows for more flexible restoration options.
   - `-b`: Includes large objects (blobs) in the backup, if any.
   - `-v`: Enables verbose mode, which provides detailed output during the backup process.
   - `-f backup_filename.backup`: Specifies the name of the backup file to be created. Replace `backup_filename.backup` with your desired file name.

3. **Enter the Password**: You will be prompted to enter the password for the `kubiu_user` role. Check the .env file for passwords.

4. **Verify Backup Creation**: Ensure that the backup file (`backup_filename.backup`) has been created in the directory you specified.


## 2. Restoring from a Backup

To restore your PostgreSQL database from a backup, use the `pg_restore` command. Follow these steps:

1. **Open a Terminal**: Access your terminal or command line interface.

2. **Run the Restore Command**: Use the following command to restore your database:

   ```bash
   pg_restore -h localhost -U kubiu_user -d kubiu_outfitters_db -v backup_filename.backup
   ```

   ### Command Explanation:

   - `pg_restore`: The PostgreSQL utility used to restore a database from a backup file.
   - `-h localhost`: Specifies the host where your PostgreSQL server is running. `localhost` refers to your local machine.
   - `-U kubiu_user`: Specifies the PostgreSQL user to connect as. Replace `kubiu_user` with your actual username.
   - `-d kubiu_outfitters_db`: Specifies the name of the database to restore into. Replace `kubiu_outfitters_db` with your actual database name.
   - `-v`: Enables verbose mode, which provides detailed output during the restoration process.
   - `backup_filename.backup`: Specifies the backup file to restore from. Replace `backup_filename.backup` with the name of your backup file.

3. **Enter the Password**: You will be prompted to enter the password for the `kubiu_user` role.

4. **Verify Restoration**: Check that the database has been restored correctly by inspecting the contents of your database.

## Credits

Author: Joseph Njoroge  
Email: [ramosnjoro@gmail.com](mailto:ramosnjoro@gmail.com)