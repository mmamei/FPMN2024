def read_template(file='gps_logger/leaflet.html'):
    with open(file) as f:
        t = f.read()
    return t

def write_file(testo, file='gps_logger/map.html'):
    with open(file, 'w') as f:
        f.write(testo)