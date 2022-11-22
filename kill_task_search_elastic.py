from elasticsearch import Elasticsearch

a = 300000000000 #nanosec

es = Elasticsearch("http://localhost:9200", http_auth=('user','pass'))
resp = es.tasks.list(actions='*/search',group_by='parents',detailed='true')

for k, v in resp.items():
    for k1, v1 in v.items():
        kk = v1.get('description')
        print('Search bad task search ' + k1 + ' - ' + kk.split()[0]) #id task and index name
        sec = int(v1.get('running_time_in_nanos'))
        if sec > a:
            print("Kill task " +  es.tasks.cancel(task_id=k1)) #kill task run over 5min
    else:
        print("Live")
        print('-------------------------------------------------')


