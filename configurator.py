import yaml,os

conf = {
	"rules_folder": "mounted_rules/",
	"run_every": {
		"minutes": 1
	},
	"es_host": os.environ.get('ES_HOST', 'localhost'),
	"es_port": int(os.environ.get('ES_PORT', '9200')),
	"use_ssl": bool(os.environ.get('USE_SSL', 'False') == 'True'),
	"writeback_index": "elastalert_status",
	"alert_time_limit": {
		"days": 2
	},
	"buffer_time": {
 		"minutes": int(os.environ.get('BUFFER_TIME', '15'))
	}
}

with open('config.yaml', 'w') as configfile:
	configfile.write(yaml.dump(conf, default_flow_style=False))