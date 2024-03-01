import os
import autotwin_gmglib as gmg

config_path = os.path.join("pizza-line-v3", "config.json")
config = gmg.load_config(config_path)
gmg.import_log(config)
log = gmg.load_log(config)
model = gmg.generate_model(log, config)
gmg.save_model(model, config)
model = gmg.load_model(config)
gmg.show_model(model)
gmg.export_model(model, config)
