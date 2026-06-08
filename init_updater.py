{
  "bomFormat" : "CycloneDX",
  "specVersion" : "1.5",
  "serialNumber" : "urn:uuid:291805c2-3324-43ba-abe4-7e8c11e881d8",
  "version" : 1,
  "metadata" : {
    "timestamp" : "2026-06-08T20:35:13Z",
    "tools" : [
      {
        "vendor" : "OWASP",
        "name" : "Dependency-Track",
        "version" : "4.14.2"
      }
    ],
    "component" : {
      "type" : "application",
      "bom-ref" : "16397239-aff6-4559-a954-a47b592b33df",
      "name" : "commons-lang__rel/commons-lang-3.17.0-orig",
      "version" : ""
    }
  },
  "components" : [
    {
      "type" : "library",
      "bom-ref" : "a5ca355e-55c3-43a3-b887-2e5b8894d266",
      "name" : "numpy",
      "version" : "1.19.0",
      "purl" : "pkg:pypi/numpy@1.19.0"
    }
  ],
  "dependencies" : [
    {
      "ref" : "16397239-aff6-4559-a954-a47b592b33df",
      "dependsOn" : [ ]
    },
    {
      "ref" : "a5ca355e-55c3-43a3-b887-2e5b8894d266",
      "dependsOn" : [ ]
    }
  ]
}
