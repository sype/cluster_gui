# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
import MySQLdb
from  clusterlib.lib import  *





def monitor_cluster(request, node):



        if node == 'node02':
            cur = db2.cursor()

            node = node

        else:
            cur = db.cursor()

        dict = {}

        #message = "NODE01"


 # Use all the SQL you like
        cur.execute("SHOW status LIKE 'wsrep%';")

        listing = cur.fetchall()


        wsrep_cluster_size = listing[31][0]
        wsrep_cluster_size_val = listing[31][1]
        cluster_uid = listing[0][0]
        cluster_uid_val = listing[1][1]
        local_state = listing[25][0]
        local_state_val  = listing[25][1]
        local_comment = listing[26][0]
        local_comment_val = listing[26][1]
        wsrep_connected = listing[34][0]
        wsrep_connected_val = listing[34][1]
        wsrep_ready = listing[39][0]
        wsrep_ready_val = listing[39][1]


        bad = '/static/img/wrong.png'
        good = '/static/img/good.png'

        img_open = good
        img_local_state = good
        img_comment = good
        img_size = good



        if local_comment_val != 'Synced':


            alerte_comment = 'critical_cluster'
            img_comment = bad
        else:
            alerte_comment = 'row_status'





        if wsrep_cluster_size_val != '2':
            #message_nb_node = 'Node are running in stand alone mode'
            alerte_size = 'critical_cluster'
            img_size = bad
        else:
            alerte_size = 'row_status'




        if wsrep_ready_val != 'ON':
            message_cluster_health = 'Cluster is actually down'
            alerte_open = 'critical_cluster'
            img_open = bad
        else:
            alerte_open = 'row_status'


        if local_state_val != '4':
            alerte_local_state = 'critical_cluster'
            img_local_state = bad
        else :
            alerte_local_state = 'row_status'



        list_of_queries = running_queries(request, node)


        return render_to_response('landing.html', {'dict': dict,'message':cluster_uid,
                                                   'cluster_uid_val':cluster_uid_val, 'local_state':local_state,
                                                   'local_state_val':local_state_val, 'local_comment':local_comment,
                                                   'local_comment_val':local_comment_val,'wsrep_connected':wsrep_connected,
                                                   'wsrep_cluster_size':wsrep_cluster_size,'wsrep_cluster_size_val':wsrep_cluster_size_val ,
                                                   'wsrep_ready':wsrep_ready,'wsrep_ready_val':wsrep_ready_val , 'alerte_size':alerte_size, ' alerte_comment': alerte_comment,
                                                   'alerte_open':alerte_open, 'alerte_local_state':alerte_local_state,
                                                   'img_local_state':img_local_state,'list_of_queries':list_of_queries,
                                                   'img_comment':img_comment, 'img_size':img_size, 'img_open':img_open,
                                                   'node':node,
                                                   'listing':listing}, context_instance=RequestContext(request))





def running_queries(request, node):
        keys = ['wsrep_OSU_method','wsrep_auto_increment_contro','wsrep_causal_reads',
                'wsrep_certify_nonPK','wsrep_cluster_address','wsrep_cluster_name',
                'wsrep_convert_LOCK_to_trx','wsrep_data_home_dir','wsrep_dbug_option','wsrep_debug',
                'wsrep_drupal_282555_workaround','wsrep_forced_binlog_format','wsrep_log_conflicts',
                'wsrep_max_ws_rows','wsrep_max_ws_size','wsrep_mysql_replication_bundle',
                'wsrep_node_address','wsrep_node_incoming_address','wsrep_node_name','wsrep_notify_cmd',
                'wsrep_on','wsrep_provider','wsrep_provider_options','wsrep_recover','wsrep_replicate_myisam',
                'wsrep_retry_autocommit','wsrep_slave_threads','wsrep_sst_auth','wsrep_sst_donor','wsrep_sst_donor_rejects_queries',
                'wsrep_sst_method','wsrep_sst_receive_address','wsrep_start_position']





        if node == 'node02':
            cur = db2.cursor()
        else:
            cur = db.cursor()

        cur.execute("SHOW variables LIKE 'wsrep%';")
        list_of_queries  =  cur.fetchall()



        return list_of_queries












def home(request):
    message = "cluster_monitoring"

    return render_to_response('base2.html', {'title': message}, context_instance=RequestContext(request))



