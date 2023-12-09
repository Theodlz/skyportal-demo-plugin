### SkyPortal Demo plugin

This is an example of a microservice plugin for SkyPortal.

To add it to a SkyPortal instance, simply edit it's config.yaml file's plugin section to include the following:

```yaml
plugins:
  demo:
    url: https://github.com/Theodlz/skyportal-demo-plugin.git
    branch: main
    params:
      demo_param: "Demo microservice plugin"
```