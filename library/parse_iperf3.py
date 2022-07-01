#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = r"""
---
module: parse_iperf3

short_description: This module uses host iperf3 and parses output and provides the result back as parsed dict

version_added: "1.0.0"

description: This is a custom module to run iperf3 test against a destination IP and print the results in readable format and for use in later stages of ansible plays

options:
    dest:
        description: The destination IP to run iperf3 against
        required: true
        type: str
    time:
        description: time in seconds to transmit for
        required: false
        type: int
        default: 5
    port:
        description: server port to connect to
        required: false
        type: int
    bind:
        description: bind to interface
        required: false
        type: str
    udp:
        description: use iperf3 in udp mode
        required: false
        type: boolean
    interval:
        description: interval between throughput reports in seconds
        required: false
        type: int
    bitrate:
        description:
        - target bitrate in bits/sec
        - possible to use [KMG][/] (slash for packet count for burst mode)
        required: false
        type: str
    length:
        description:
        - length of buffer to read or write
        - possible to use [KMG]
        required: false
        type: str
    streams:
        description: number of parallel streams to run
        required: false
        type: int
    reverse:
        description: whether to run iperf3 in reverse mode
        required: false
        type: boolean
    connection_timeout:
        description: connection timeout in seconds
        required: false
        type: int

author:
    - Hemant Zope (@zhemant)
"""

EXAMPLES = r"""
- name: Test iperf3 udp
  parse_iperf3:
    dest: 127.0.0.1
    udp: true

- name: Test iperf3 tcp reverse
  parse_iperf3:
    dest: 127.0.0.1
    reverse: true

- name: Test iperf3 parallel 5 streams
  parse_iperf3:
    dest: 127.0.0.1
    parallel: 5
"""

RETURN = r"""
# These are examples of possible return values, and in general should use other names for return values.
stdout_lines:
    description: The command standard output
    returned: always
    type: list of string
    sample: '[
            "{",
                "\t\"start\":\t{",
                "\t\t\"connected\":\t[{",
                "\t\t\t\t\"socket\":\t5,",
                "\t\t\t\t\"local_host\":\t\"127.0.0.1\",",
                "\t\t\t\t\"local_port\":\t35020,",
                "\t\t\t\t\"remote_host\":\t\"127.0.0.1\",",
                "\t\t\t\t\"remote_port\":\t5201",
                "\t\t\t}],",
                "\t\t\"version\":\t\"iperf 3.7\",",
                "\t\t\"system_info\":\t\"Linux thinkpad14 5.15.0-33-generic #34~20.04.1-Ubuntu SMP Thu May 19 15:51:16 UTC 2022 x86_64\",",
                "\t\t\"timestamp\":\t{",
                "\t\t\t\"time\":\t\"Fri, 01 Jul 2022 11:19:15 GMT\",",
                "\t\t\t\"timesecs\":\t1656674355",
                "\t\t},",
                "\t\t\"connecting_to\":\t{",
                "\t\t\t\"host\":\t\"127.0.0.1\",",
                "\t\t\t\"port\":\t5201",
                "\t\t},",
                "\t\t\"cookie\":\t\"qxyxptpi54xjfo33wsev7gzl4ikyc2fozgml\",",
                "\t\t\"tcp_mss_default\":\t32768,",
                "\t\t\"sock_bufsize\":\t0,",
                "\t\t\"sndbuf_actual\":\t16384,",
                "\t\t\"rcvbuf_actual\":\t131072,",
                "\t\t\"test_start\":\t{",
                "\t\t\t\"protocol\":\t\"TCP\",",
                "\t\t\t\"num_streams\":\t1,",
                "\t\t\t\"blksize\":\t131072,",
                "\t\t\t\"omit\":\t0,",
                "\t\t\t\"duration\":\t2,",
                "\t\t\t\"bytes\":\t0,",
                "\t\t\t\"blocks\":\t0,",
                "\t\t\t\"reverse\":\t0,",
                "\t\t\t\"tos\":\t0",
                "\t\t}",
                "\t},",
                "\t\"intervals\":\t[{",
                "\t\t\t\"streams\":\t[{",
                "\t\t\t\t\t\"socket\":\t5,",
                "\t\t\t\t\t\"start\":\t0,",
                "\t\t\t\t\t\"end\":\t1.000104,",
                "\t\t\t\t\t\"seconds\":\t1.0001039505004883,",
                "\t\t\t\t\t\"bytes\":\t4341104640,",
                "\t\t\t\t\t\"bits_per_second\":\t34725227415.230614,",
                "\t\t\t\t\t\"retransmits\":\t0,",
                "\t\t\t\t\t\"snd_cwnd\":\t1047728,",
                "\t\t\t\t\t\"rtt\":\t40,",
                "\t\t\t\t\t\"rttvar\":\t2,",
                "\t\t\t\t\t\"pmtu\":\t65535,",
                "\t\t\t\t\t\"omitted\":\tfalse,",
                "\t\t\t\t\t\"sender\":\ttrue",
                "\t\t\t\t}],",
                "\t\t\t\"sum\":\t{",
                "\t\t\t\t\"start\":\t0,",
                "\t\t\t\t\"end\":\t1.000104,",
                "\t\t\t\t\"seconds\":\t1.0001039505004883,",
                "\t\t\t\t\"bytes\":\t4341104640,",
                "\t\t\t\t\"bits_per_second\":\t34725227415.230614,",
                "\t\t\t\t\"retransmits\":\t0,",
                "\t\t\t\t\"omitted\":\tfalse,",
                "\t\t\t\t\"sender\":\ttrue",
                "\t\t\t}",
                "\t\t}, {",
                "\t\t\t\"streams\":\t[{",
                "\t\t\t\t\t\"socket\":\t5,",
                "\t\t\t\t\t\"start\":\t1.000104,",
                "\t\t\t\t\t\"end\":\t2.000218,",
                "\t\t\t\t\t\"seconds\":\t1.0001139640808105,",
                "\t\t\t\t\t\"bytes\":\t4331929600,",
                "\t\t\t\t\t\"bits_per_second\":\t34651487775.047,",
                "\t\t\t\t\t\"retransmits\":\t0,",
                "\t\t\t\t\t\"snd_cwnd\":\t1047728,",
                "\t\t\t\t\t\"rtt\":\t31,",
                "\t\t\t\t\t\"rttvar\":\t10,",
                "\t\t\t\t\t\"pmtu\":\t65535,",
                "\t\t\t\t\t\"omitted\":\tfalse,",
                "\t\t\t\t\t\"sender\":\ttrue",
                "\t\t\t\t}],",
                "\t\t\t\"sum\":\t{",
                "\t\t\t\t\"start\":\t1.000104,",
                "\t\t\t\t\"end\":\t2.000218,",
                "\t\t\t\t\"seconds\":\t1.0001139640808105,",
                "\t\t\t\t\"bytes\":\t4331929600,",
                "\t\t\t\t\"bits_per_second\":\t34651487775.047,",
                "\t\t\t\t\"retransmits\":\t0,",
                "\t\t\t\t\"omitted\":\tfalse,",
                "\t\t\t\t\"sender\":\ttrue",
                "\t\t\t}",
                "\t\t}],",
                "\t\"end\":\t{",
                "\t\t\"streams\":\t[{",
                "\t\t\t\t\"sender\":\t{",
                "\t\t\t\t\t\"socket\":\t5,",
                "\t\t\t\t\t\"start\":\t0,",
                "\t\t\t\t\t\"end\":\t2.000218,",
                "\t\t\t\t\t\"seconds\":\t2.000218,",
                "\t\t\t\t\t\"bytes\":\t8673034240,",
                "\t\t\t\t\t\"bits_per_second\":\t34688355929.20372,",
                "\t\t\t\t\t\"retransmits\":\t0,",
                "\t\t\t\t\t\"max_snd_cwnd\":\t1047728,",
                "\t\t\t\t\t\"max_rtt\":\t40,",
                "\t\t\t\t\t\"min_rtt\":\t31,",
                "\t\t\t\t\t\"mean_rtt\":\t35,",
                "\t\t\t\t\t\"sender\":\ttrue",
                "\t\t\t\t},",
                "\t\t\t\t\"receiver\":\t{",
                "\t\t\t\t\t\"socket\":\t5,",
                "\t\t\t\t\t\"start\":\t0,",
                "\t\t\t\t\t\"end\":\t2.000229,",
                "\t\t\t\t\t\"seconds\":\t2.000218,",
                "\t\t\t\t\t\"bytes\":\t8673034240,",
                "\t\t\t\t\t\"bits_per_second\":\t34688165165.0886,",
                "\t\t\t\t\t\"sender\":\ttrue",
                "\t\t\t\t}",
                "\t\t\t}],",
                "\t\t\"sum_sent\":\t{",
                "\t\t\t\"start\":\t0,",
                "\t\t\t\"end\":\t2.000218,",
                "\t\t\t\"seconds\":\t2.000218,",
                "\t\t\t\"bytes\":\t8673034240,",
                "\t\t\t\"bits_per_second\":\t34688355929.20372,",
                "\t\t\t\"retransmits\":\t0,",
                "\t\t\t\"sender\":\ttrue",
                "\t\t},",
                "\t\t\"sum_received\":\t{",
                "\t\t\t\"start\":\t0,",
                "\t\t\t\"end\":\t2.000229,",
                "\t\t\t\"seconds\":\t2.000229,",
                "\t\t\t\"bytes\":\t8673034240,",
                "\t\t\t\"bits_per_second\":\t34688165165.0886,",
                "\t\t\t\"sender\":\ttrue",
                "\t\t},",
                "\t\t\"cpu_utilization_percent\":\t{",
                "\t\t\t\"host_total\":\t99.865710211106546,",
                "\t\t\t\"host_user\":\t0.59665526241570144,",
                "\t\t\t\"host_system\":\t99.269005119455628,",
                "\t\t\t\"remote_total\":\t3.3332492297829743,",
                "\t\t\t\"remote_user\":\t0.078029535569388311,",
                "\t\t\t\"remote_system\":\t3.2552196942135869",
                "\t\t},",
                "\t\t\"sender_tcp_congestion\":\t\"cubic\",",
                "\t\t\"receiver_tcp_congestion\":\t\"cubic\"",
                "\t}",
            "}"
    ]'
stderr:
    description: The command standard error
    returned: always
    type: string
    sample: 'unable to connect to server'
rc:
    description: The command return code (0 means success)
    returned: always
    type: int
    sample: 0
stdout:
    description: The command standard output split in lines
    returned: always
    type: list of strings
    sample: '{\n\t\"start\":\t{\n\t\t\"connected\":\t[{\n\t\t\t\t\"socket\":\t5,\n\t\t\t\t\"local_host\":\t\"127.0.0.1\",\n\t\t\t\t\"local_port\":\t35020,\n\t\t\t\t\"remote_host\":\t\"127.0.0.1\",\n\t\t\t\t\"remote_port\":\t5201\n\t\t\t}],\n\t\t\"version\":\t\"iperf 3.7\",\n\t\t\"system_info\":\t\"Linux thinkpad14 5.15.0-33-generic #34~20.04.1-Ubuntu SMP Thu May 19 15:51:16 UTC 2022 x86_64\",\n\t\t\"timestamp\":\t{\n\t\t\t\"time\":\t\"Fri, 01 Jul 2022 11:19:15 GMT\",\n\t\t\t\"timesecs\":\t1656674355\n\t\t},\n\t\t\"connecting_to\":\t{\n\t\t\t\"host\":\t\"127.0.0.1\",\n\t\t\t\"port\":\t5201\n\t\t},\n\t\t\"cookie\":\t\"qxyxptpi54xjfo33wsev7gzl4ikyc2fozgml\",\n\t\t\"tcp_mss_default\":\t32768,\n\t\t\"sock_bufsize\":\t0,\n\t\t\"sndbuf_actual\":\t16384,\n\t\t\"rcvbuf_actual\":\t131072,\n\t\t\"test_start\":\t{\n\t\t\t\"protocol\":\t\"TCP\",\n\t\t\t\"num_streams\":\t1,\n\t\t\t\"blksize\":\t131072,\n\t\t\t\"omit\":\t0,\n\t\t\t\"duration\":\t2,\n\t\t\t\"bytes\":\t0,\n\t\t\t\"blocks\":\t0,\n\t\t\t\"reverse\":\t0,\n\t\t\t\"tos\":\t0\n\t\t}\n\t},\n\t\"intervals\":\t[{\n\t\t\t\"streams\":\t[{\n\t\t\t\t\t\"socket\":\t5,\n\t\t\t\t\t\"start\":\t0,\n\t\t\t\t\t\"end\":\t1.000104,\n\t\t\t\t\t\"seconds\":\t1.0001039505004883,\n\t\t\t\t\t\"bytes\":\t4341104640,\n\t\t\t\t\t\"bits_per_second\":\t34725227415.230614,\n\t\t\t\t\t\"retransmits\":\t0,\n\t\t\t\t\t\"snd_cwnd\":\t1047728,\n\t\t\t\t\t\"rtt\":\t40,\n\t\t\t\t\t\"rttvar\":\t2,\n\t\t\t\t\t\"pmtu\":\t65535,\n\t\t\t\t\t\"omitted\":\tfalse,\n\t\t\t\t\t\"sender\":\ttrue\n\t\t\t\t}],\n\t\t\t\"sum\":\t{\n\t\t\t\t\"start\":\t0,\n\t\t\t\t\"end\":\t1.000104,\n\t\t\t\t\"seconds\":\t1.0001039505004883,\n\t\t\t\t\"bytes\":\t4341104640,\n\t\t\t\t\"bits_per_second\":\t34725227415.230614,\n\t\t\t\t\"retransmits\":\t0,\n\t\t\t\t\"omitted\":\tfalse,\n\t\t\t\t\"sender\":\ttrue\n\t\t\t}\n\t\t}, {\n\t\t\t\"streams\":\t[{\n\t\t\t\t\t\"socket\":\t5,\n\t\t\t\t\t\"start\":\t1.000104,\n\t\t\t\t\t\"end\":\t2.000218,\n\t\t\t\t\t\"seconds\":\t1.0001139640808105,\n\t\t\t\t\t\"bytes\":\t4331929600,\n\t\t\t\t\t\"bits_per_second\":\t34651487775.047,\n\t\t\t\t\t\"retransmits\":\t0,\n\t\t\t\t\t\"snd_cwnd\":\t1047728,\n\t\t\t\t\t\"rtt\":\t31,\n\t\t\t\t\t\"rttvar\":\t10,\n\t\t\t\t\t\"pmtu\":\t65535,\n\t\t\t\t\t\"omitted\":\tfalse,\n\t\t\t\t\t\"sender\":\ttrue\n\t\t\t\t}],\n\t\t\t\"sum\":\t{\n\t\t\t\t\"start\":\t1.000104,\n\t\t\t\t\"end\":\t2.000218,\n\t\t\t\t\"seconds\":\t1.0001139640808105,\n\t\t\t\t\"bytes\":\t4331929600,\n\t\t\t\t\"bits_per_second\":\t34651487775.047,\n\t\t\t\t\"retransmits\":\t0,\n\t\t\t\t\"omitted\":\tfalse,\n\t\t\t\t\"sender\":\ttrue\n\t\t\t}\n\t\t}],\n\t\"end\":\t{\n\t\t\"streams\":\t[{\n\t\t\t\t\"sender\":\t{\n\t\t\t\t\t\"socket\":\t5,\n\t\t\t\t\t\"start\":\t0,\n\t\t\t\t\t\"end\":\t2.000218,\n\t\t\t\t\t\"seconds\":\t2.000218,\n\t\t\t\t\t\"bytes\":\t8673034240,\n\t\t\t\t\t\"bits_per_second\":\t34688355929.20372,\n\t\t\t\t\t\"retransmits\":\t0,\n\t\t\t\t\t\"max_snd_cwnd\":\t1047728,\n\t\t\t\t\t\"max_rtt\":\t40,\n\t\t\t\t\t\"min_rtt\":\t31,\n\t\t\t\t\t\"mean_rtt\":\t35,\n\t\t\t\t\t\"sender\":\ttrue\n\t\t\t\t},\n\t\t\t\t\"receiver\":\t{\n\t\t\t\t\t\"socket\":\t5,\n\t\t\t\t\t\"start\":\t0,\n\t\t\t\t\t\"end\":\t2.000229,\n\t\t\t\t\t\"seconds\":\t2.000218,\n\t\t\t\t\t\"bytes\":\t8673034240,\n\t\t\t\t\t\"bits_per_second\":\t34688165165.0886,\n\t\t\t\t\t\"sender\":\ttrue\n\t\t\t\t}\n\t\t\t}],\n\t\t\"sum_sent\":\t{\n\t\t\t\"start\":\t0,\n\t\t\t\"end\":\t2.000218,\n\t\t\t\"seconds\":\t2.000218,\n\t\t\t\"bytes\":\t8673034240,\n\t\t\t\"bits_per_second\":\t34688355929.20372,\n\t\t\t\"retransmits\":\t0,\n\t\t\t\"sender\":\ttrue\n\t\t},\n\t\t\"sum_received\":\t{\n\t\t\t\"start\":\t0,\n\t\t\t\"end\":\t2.000229,\n\t\t\t\"seconds\":\t2.000229,\n\t\t\t\"bytes\":\t8673034240,\n\t\t\t\"bits_per_second\":\t34688165165.0886,\n\t\t\t\"sender\":\ttrue\n\t\t},\n\t\t\"cpu_utilization_percent\":\t{\n\t\t\t\"host_total\":\t99.865710211106546,\n\t\t\t\"host_user\":\t0.59665526241570144,\n\t\t\t\"host_system\":\t99.269005119455628,\n\t\t\t\"remote_total\":\t3.3332492297829743,\n\t\t\t\"remote_user\":\t0.078029535569388311,\n\t\t\t\"remote_system\":\t3.2552196942135869\n\t\t},\n\t\t\"sender_tcp_congestion\":\t\"cubic\",\n\t\t\"receiver_tcp_congestion\":\t\"cubic\"\n\t}\n}\n"
        '
cmd:
    description: The complete command executed
    type: str
    returned: always
    sample: 'iperf3 -c 127.0.0.1 -J --connect-timeout 5000 --time 2 --parallel 1 127.0.0.1'
parsed:
    description: Dictionary of parsed output of ping
    type: dict
    returned: always
    sample: '
        {
            "local_host": "127.0.0.1",
            "local_port": 35016,
            "remote_host": "127.0.0.1",
            "remote_port": 5201,
            "total_received": "35.59 Gbps",
            "total_sent": "35.59 Gbps",
            "type": "receiver"
        }

    '
"""

from ansible.module_utils.basic import AnsibleModule
import json


def bitstoKMGT(b, israw=0):
    if israw:
        return b

    b = float(b)
    Kb = float(1000)
    Mb = float(Kb**2)
    Gb = float(Kb**3)
    Tb = float(Kb**4)

    if b < Kb:
        return "{0} {1}".format(b, "Bytes" if 0 == b > 1 else "Byte")
    elif Kb <= b < Mb:
        return "{0:.2f} Kbps".format(b / Kb)
    elif Mb <= b < Gb:
        return "{0:.2f} Mbps".format(b / Mb)
    elif Gb <= b < Tb:
        return "{0:.2f} Gbps".format(b / Gb)
    elif Tb <= b:
        return "{0:.2f} Tbps".format(b / Tb)


def main():

    fields = {
        "dest": {"required": True, "type": "str"},
        "time": {"required": False, "type": "int", "default": 5},
        "port": {"required": False, "type": "int"},
        "bind": {"required": False, "type": "str"},
        "udp": {"required": False, "type": "bool"},
        "interval": {"required": False, "type": "int"},
        "bitrate": {"required": False, "type": "str"},
        "length": {"required": False, "type": "str"},
        "streams": {"required": False, "type": "int", "default": 1},
        "reverse": {"required": False, "type": "bool"},
        "connection_timeout": {"required": False, "type": "int", "default": 5}
    }

    module = AnsibleModule(argument_spec=fields)

    # params
    dest = module.params["dest"]
    time = module.params["time"]
    port = module.params["port"]
    bind = module.params["bind"]
    udp = module.params["udp"]
    interval = module.params["interval"]
    bitrate = module.params["bitrate"]
    length = module.params["length"]
    streams = module.params["streams"]
    reverse = module.params["reverse"]
    timeout = module.params["connection_timeout"]

    # build command
    cmd = ["iperf3"]

    cmd.append(f"-c { dest }")

    cmd.append(f"-J")


    if timeout:
        cmd.append(f"--connect-timeout { timeout *1000 }")
    if time:
        cmd.append(f"--time { time }")
    if port:
        cmd.append(f"--port { port }")
    if bind:
        cmd.append(f"--bind { bind }")
    if udp:
        cmd.append(f"--udp")
    if interval:
        cmd.append(f"--interval { interval }")
    if bitrate:
        cmd.append(f"--bitrate { bitrate }")
    if length:
        cmd.append(f"--length { length }")
    if streams:
        cmd.append(f"--parallel { streams }")
    if reverse:
        cmd.append(f"--reverse")

    # command as str
    run_cmd = " ".join(cmd)
    rc, out, err = module.run_command(run_cmd)

    if rc == 1:
        msg = ""
        if "unable to connect to server" in out:
            msg = "unable to connect to server"
        module.fail_json(changed=False, stdout=out, rc=rc, stderr=err, cmd=run_cmd, msg=msg)

    if rc == 0:
        payload = json.loads(out)
        res = dict()
        res["local_host"] = payload["start"]["connected"][0]["local_host"]
        res["local_port"] = payload["start"]["connected"][0]["local_port"]
        res["remote_host"] = payload["start"]["connected"][0]["remote_host"]
        res["remote_port"] = payload["start"]["connected"][0]["remote_port"]

        if udp:
            issender = payload["end"]["sum"]["sender"]
            bps = payload["end"]["sum"]["bits_per_second"]
            if issender:
                res["total_sent"] = bitstoKMGT(bps)
                res["type"] = "sender"
            else:
                res["total_received"] = bitstoKMGT(bps)
                res["type"] = "receiver"

        else:
            res["total_received"] = bitstoKMGT(
                payload["end"]["sum_received"]["bits_per_second"]
            )
            res["total_sent"] = bitstoKMGT(
                payload["end"]["sum_sent"]["bits_per_second"]
            )
            issender = payload["end"]["sum_sent"]["sender"]
            if issender:
                res["type"] = "sender"
            else:
                res["type"] = "receiver"

        module.exit_json(
            changed=False, stdout=out, rc=rc, stderr=err, cmd=run_cmd, parsed=res
        )

    module.exit_json(changed=False, stdout=out, rc=rc, stderr=err, cmd=run_cmd)


if __name__ == "__main__":
    main()
