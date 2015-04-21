# Background
The PaaS solution space is crowded with new offerings springing up every other month which will only increase with the advent of container technologies like Docker, LXD etc., Naturally there is a lot of fragmentation with providers competing over features, services and ease of application development on the platform.

There are multiple commercial PaaS offerings in existence such as Heroku, OpenShift, CloudFoundry etc., Each of these platforms support different languages such as Java, Python, Ruby and offer various services such as datastores, email, caches, monitoring, payment gateways and so on. Writing an application for a PaaS platform has also become considerably simpler and easier over time.However, there is a problem of vendor lock-in. Migrating an existing application from one PaaS platform to another is substantially difficult, if not impossible. [OASIS CAMP](http://docs.oasis-open.org/camp/camp-spec/v1.1/camp-spec-v1.1.pdf) (Cloud application management for Platforms) is an ongoing effort to standardize management APIs and application specification and format, so that applications can be interoperable across compliant PaaS platforms.

"libpaas" aims to provide a unified and extensible library framework to communicate with multiple PaaS platforms by standardizing on CAMP v1.1 model for application packaging and structure. A CLI toolkit is also built on top of this framework to demonstrate application lifecycle management on different platforms without worrying about platform intricacies. The aim is to evolve this into an opensource, stable library framework along the lines of libcloud and jcloud for PaaS platforms.

Here is a high level block diagram of libpaas.

![libpaas-block-diagram](https://lh5.googleusercontent.com/-izzBMQo91zw/VTZ6ciuMFpI/AAAAAAAAeV4/KHIDKAyZpHo/w1214-h508-no/libpaas-block-diagram.png)

# Usage

* Install it from pip
```
$ pip install paascli

```

* Type "paascli" to access the CLI toolkit

```
$ paascli
Usage: paascli [OPTIONS] COMMAND [ARGS]...

  Manage your applications across PaaS providers

Options:
  --help  Show this message and exit.

Commands:
  app       Manage applications
  provider  Manage paas providers
  refresh   Refresh local cache from cloud
  reset     Reset configuration and local cache

```

> **Note:**
Currently heroku and openshift drivers are the only available drivers. Limited testing is done using a sample [python wsgi application](https://github.com/hvishwanath/libpaas-sampleapp).

