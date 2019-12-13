# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 10/22/2018
"""

# !/usr/bin/env python

import os

import paramiko


def ping(host, cnt):
	'''ping test'''
	import subprocess, traceback, platform
	print
	platform.system()
	if platform.system() == 'Windows':
		cmd = 'ping -n %d %s' % (cnt, host)
	else:
		cmd = 'ping -c %d %s' % (cnt, host)

	try:
		p = subprocess.Popen(args = cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
		(stdoutput, erroutput) = p.communicate()
	# print stdoutput
	except Exception, e:
		traceback.print_exc()

	if platform.system() == 'Windows':
		return stdoutput.find('Received = %d' % cnt) >= 0
	else:
		return stdoutput.find('%d received' % cnt) >= 0


def collect_platform_info(ip, fd):
	fd.write("%-20s" % ip)

	if not ping(ip, 3):
		fd.write("--\n")
		return

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, 22, "root", "infinera")

	stdin, stdout, stderr = ssh.exec_command("esxcfg-info -w | grep 'HV Support'")
	for l in stdout.readlines():
		fd.write("%s\n" % l.strip())

	ssh.close()


if __name__ == "__main__":
	result_file = "/home/infinera/server_stats.txt"
	os.remove(result_file)
	fd_res = open(result_file, "w")
	fd_res.write("%-20s|%s\n" % ("HV IP", "VT-X"))
	fd_res.write(80 * "-")
	fd_res.write("\n")

	fd_ips = open("/home/infinera/server_list.txt", "r")
	for l in fd_ips.readlines():
		ip = l.strip()
		collect_platform_info(ip, fd_res)

	fd_ips.close()
	fd_res.close()
