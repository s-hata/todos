#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(url='mysql://todos:todos@192.168.99.100:3306/todos', debug='False', repository='db_migration_repo/')
