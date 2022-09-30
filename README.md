# jemaloc - rpm specs

Custom jemalloc build for NetXMS.

## Build

```sh
docker build -t netxms-rpm-builder docker
docker run --cap-add=SYS_ADMIN -it --rm  -v $(pwd):/build -v $(pwd)/result:/result netxms-rpm-builder
docker image rm netxms-rpm-builder

# Cache dependencies between builds
#docker run --cap-add=SYS_ADMIN -it --rm -v $(pwd)/cache:/var/cache/mock -v $(pwd):/build -v $(pwd)/result:/result netxms-rpm-builder
```
