import platform
import cpuinfo
import subprocess
from flask import jsonify


def get_proc_model():
    cpu = cpuinfo.get_cpu_info()

    cpu_model = {"model": cpu['model']}

    return jsonify(cpu_model)


def get_proc_cache(level):
    if level == "l2":
        cach = cpuinfo.get_cpu_info()['l2_cache_size']
        cach_cpu = {"l2": cache}
        return jsonify(cache_info)
    if level == "l3":
        cach = cpuinfo.get_cpu_info()['l3_cache_size']
        cach_cpu = {"l3": cache}
        return jsonify(cach_cpu)
    else:
        cach_cpu = {"l2": cpuinfo.get_cpu_info()['l2_cache_size'],
                      "l3": cpuinfo.get_cpu_info()['l3_cache_size']}
        return jsonify({"cache l2/l3": cach_cpu})
