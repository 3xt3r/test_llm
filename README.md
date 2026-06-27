1:50:50 [ERROR] stderr: Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/instruments/extract/extract.py", line 9, in <module>
    import rarfile
ModuleNotFoundError: No module named 'rarfile'
2026-06-27 11:50:50 | ERROR   |     [FAIL] scanner.py: exited with code 1
2026-06-27 11:50:50 | INFO    |   moving results: /home/kali/Desktop/jobs/express/jobs/f9738d11062b4a5baeaaa78fde8390f5 -> /home/kali/Desktop/results/2026-06-27/express__v4.22.2
2026-06-27 11:50:50 | INFO    | [distrib] started thread for express / v4.22.2 / NDR_alt
2026-06-27 11:50:50 | ERROR   |   [FAIL] express / v4.22.2: exited with code 1
2026-06-27 11:50:50 | INFO    | [distrib] waiting for 1 distrib thread(s) to finish...
2026-06-27 11:50:51 | INFO    | [distrib] [express__v4.22.2__NDR_alt] found orig project 'express__v4.22.2-orig' -> a837cbdd-44ee-465f-aeb7-5834b79fe86a
2026-06-27 11:50:51 | INFO    | [dt] reusing existing project 'express__v4.22.2__NDR_alt__packages':v4.22.2 -> c9de8313-e76e-4bae-a77a-8e59fd808787
2026-06-27 11:50:51 | INFO    | [distrib] [express__v4.22.2__NDR_alt] project 'express__v4.22.2__NDR_alt__packages' -> c9de8313-e76e-4bae-a77a-8e59fd808787
2026-06-27 11:50:51 | INFO    | [dt] reusing existing project 'express__v4.22.2__NDR_alt__binary':v4.22.2 -> 219e4e29-fc76-4bfe-bce3-97678bacb99d
2026-06-27 11:50:51 | INFO    | [distrib] [express__v4.22.2__NDR_alt] project 'express__v4.22.2__NDR_alt__binary' -> 219e4e29-fc76-4bfe-bce3-97678bacb99d
2026-06-27 11:50:51 | INFO    | [dt] reusing existing project 'express__v4.22.2__NDR_alt__repack':v4.22.2 -> 134bf438-f8a0-4ef9-903e-95a4691d601d
2026-06-27 11:50:51 | INFO    | [distrib] [express__v4.22.2__NDR_alt] project 'express__v4.22.2__NDR_alt__repack' -> 134bf438-f8a0-4ef9-903e-95a4691d601d
2026-06-27 11:50:51 | INFO    | [distrib] [express__v4.22.2__NDR_alt] starting scan: /home/kali/Desktop/NDR (timeout=7200s)
Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/distrib/sbom_tool.py", line 20, in <module>
    from sbom_deb import cmd_deb, build_deb_parser
ImportError: cannot import name 'build_deb_parser' from 'sbom_deb' (/home/kali/Desktop/oss_checks/distrib/sbom_deb.py)
2026-06-27 11:50:51 | ERROR   | [distrib] [express__v4.22.2__NDR_alt] scan failed rc=1
2026-06-27 11:50:51 | INFO    | [distrib] all distrib threads finished
2026-06-27 11:50:51 | INFO    | run log written: /home/kali/Desktop/results/2026-06-27/run.log
2026-06-27 11:50:51 | ERROR   | 1/1 scan(s) failed
