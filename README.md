2026-06-27 12:00:41 | INFO    | [dt] reusing existing project 'express__v4.22.2__NDR_alt__repack':v4.22.2 -> 134bf438-f8a0-4ef9-903e-95a4691d601d
2026-06-27 12:00:41 | INFO    | [distrib] [express__v4.22.2__NDR_alt] project 'express__v4.22.2__NDR_alt__repack' -> 134bf438-f8a0-4ef9-903e-95a4691d601d
2026-06-27 12:00:41 | INFO    | [distrib] [express__v4.22.2__NDR_alt] starting scan: /home/kali/Desktop/NDR (timeout=7200s)
Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/distrib/sbom_tool.py", line 21, in <module>
    from sbom_rpm import (
  File "/home/kali/Desktop/oss_checks/distrib/sbom_rpm.py", line 20, in <module>
    from sbom_components import (
ImportError: cannot import name 'ensure_properties' from 'sbom_components' (/home/kali/Desktop/oss_checks/distrib/sbom_components.py)
2026-06-27 12:00:41 | ERROR   | [distrib] [express__v4.22.2__NDR_alt] scan failed rc=1
2026-06-27 12:00:41 | INFO    | [distrib] all distrib threads finished
2026-06-27 12:00:41 | INFO    | run log written: /home/kali/Desktop/results/2026-06-27/run.log
2026-06-27 12:00:41 | INFO    | all 1 scan(s) completed successfully
