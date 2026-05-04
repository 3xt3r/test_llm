[OK] Wrote 987 rows to /home/csecuser/jobs/4cd93d82da63430e9826417b2dd7e919/reports/licenses.xlsx
01:07:24 [INFO] task done: License Collection
01:07:24 [INFO] task start: ASM Audit
01:07:51 [WARNING] [asm] bad grep hit suspicious/too-long path component, skipping: /home/csecuser/jobs/4cd93d82da63430e9826417b2dd7e919/transitive_libs/","escapeRegExp","escapeChar","bareIdentifier","template","text","settings","oldSettings","offset","render","argument","variable","Error","e","data","fallback","idCounter"...[truncated 1231 chars]...mpact","Boolean","_flatten","difference","without","otherArrays","uniq","isSorted","seen","union","arrays","intersection","argsLength","unzip","zip","range","stop","step","ceil","chunk","count","chainResult","mixin","allExports"],"mappings"
01:07:51 [WARNING] [asm] bad grep hit suspicious/too-long path component, skipping: /home/csecuser/jobs/4cd93d82da63430e9826417b2dd7e919/transitive_libs/","escapeRegExp","escapeChar","bareIdentifier","idCounter","executeBound","sourceFunc","boundFunc","callingContext","partial","boundArgs","placeholder","bound","position",...[truncated 1176 chars]...ading","throttled","_now","remaining","clearTimeout","trailing","cancel","immediate","passed","debounced","_args","wrapper","start","criteria","left","right","Boolean","_flatten","argsLength","stop","step","ceil","range","count"],"mappings"
01:07:51 [WARNING] [asm] bad grep hit suspicious/too-long path component, skipping: /home/csecuser/jobs/4cd93d82da63430e9826417b2dd7e919/transitive_libs/","escapeRegExp","escapeChar","bareIdentifier","idCounter","executeBound","sourceFunc","boundFunc","callingContext","partial","boundArgs","placeholder","bound","position",...[truncated 1176 chars]...ading","throttled","_now","remaining","clearTimeout","trailing","cancel","immediate","passed","debounced","_args","wrapper","start","criteria","left","right","Boolean","_flatten","argsLength","stop","step","ceil","range","count"],"mappings"
Traceback (most recent call last):
  File "/home/csecuser/oss_checks/scanner.py", line 1350, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "/home/csecuser/oss_checks/scanner.py", line 1341, in main
    return pipeline_flow(
        root=root,
    ...<2 lines>...
        dt_config=dt_config,
    )
  File "/home/csecuser/oss_checks/scanner.py", line 113, in wrapper
    result = fn(*args, **kwargs)
  File "/home/csecuser/oss_checks/scanner.py", line 1130, in pipeline_flow
    asm_transitive_future = run_asm_audit_for_target.submit(
        job_dir=paths.asm_dir,
    ...<2 lines>...
        wait_for=[transitive_future],
    )
  File "/home/csecuser/oss_checks/scanner.py", line 80, in submit
    value = self.fn(*args, **kwargs)
  File "/home/csecuser/oss_checks/scanner.py", line 716, in run_asm_audit_for_target
    found = run_asm_audit(scan_root=scan_root, out_file=out_file)
  File "/home/csecuser/oss_checks/asm_core/api.py", line 33, in run_asm_audit
    return write_excel_report(
        root=scan_root.resolve(),
    ...<5 lines>...
        exclude_dirs=normalize_exclude_dirs(opts.exclude_dirs),
    )
  File "/home/csecuser/oss_checks/asm_core/report.py", line 148, in write_excel_report
    rows_build_hits, rows_build_other = audit_build.collect_build_dfs(
                                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        root,
        ^^^^^
        near_after=near_after,
        ^^^^^^^^^^^^^^^^^^^^^^
        exclude_dirs=exclude_dirs,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/csecuser/oss_checks/asm_core/audit_build.py", line 79, in collect_build_dfs
    not path.is_file()
        ~~~~~~~~~~~~^^
  File "/opt/conda/lib/python3.13/pathlib/_abc.py", line 482, in is_file
    return S_ISREG(self.stat(follow_symlinks=follow_symlinks).st_mode)
                   ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/lib/python3.13/pathlib/_local.py", line 515, in stat
    return os.stat(self, follow_symlinks=follow_symlinks)
           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 36] File name too long: '/home/csecuser/jobs/4cd93d82da63430e9826417b2dd7e919/transitive_libs/","escapeRegExp","escapeChar","bareIdentifier","template","text","settings","oldSettings","offset","render","argument","variable","Error","e","data","fallback","idCounter","uniqueId","prefix","id","chain","instance","_chain","executeBound","sourceFunc","boundFunc","callingContext","partial","boundArgs","placeholder","bound","position","bind","TypeError","callArgs","isArrayLike","flatten","input","depth","strict","output","idx","j","len","bindAll","memoize","hasher","cache","address","delay","wait","setTimeout","defer","throttle","options","timeout","previous","later","leading","throttled","_now","remaining","clearTimeout","trailing","cancel","debounce","immediate","passed","debounced","_args","wrap","wrapper","negate","predicate","compose","start","after","before","memo","once","findKey","createPredicateIndexFinder","dir","array","findIndex","findLastIndex","sortedIndex","low","high","mid","createIndexFinder","predicateFind","item","indexOf","lastIndexOf","find","findWhere","each","createReduce","reducer","initial","reduce","reduceRight","filter","list","reject","every","some","fromIndex","guard","invoke","contextPath","method","pluck","where","computed","lastComputed","v","reStrSymbol","toArray","sample","last","rand","temp","shuffle","sortBy","criteria","left","right","group","behavior","partition","groupBy","indexBy","countBy","pass","size","keyInObj","pick","omit","first","compact","Boolean","_flatten","difference","without","otherArrays","uniq","isSorted","seen","union","arrays","intersection","argsLength","unzip","zip","range","stop","step","ceil","chunk","count","chainResult","mixin","allExports"],"mappings"'
(venv) csecuser@test-oss-checker:~/oss_checks$ client_loop: send disconnect: Connection reset by peer
