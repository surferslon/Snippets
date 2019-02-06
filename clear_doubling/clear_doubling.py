# -*- coding: utf-8 -*-
import psycopg2

if __name__ == '__main__':
    print 10 * '-'
    database = psycopg2.connect(
        "dbname='optima3_dixel' user='dbu_optima3' host='localhost' password='asjh3522Gfbs23x'"
    )
    cursor = database.cursor()
    result = cursor.execute('''
        delete
        from gateways_externallink out
        where (
            select count(*)
            from gateways_externallink inr
            where inr.object_id = out.object_id
            and inr.content_type_id=out.content_type_id ) > 1;
        ''')
    print 'done'
