# GitLab CI Experimental Environment

## Reference

- [GitLab Server and Pages Setup](https://blogs.networld.co.jp/entry/2022/09/12/090000)
- [GitLab Runner Setup](https://blogs.networld.co.jp/entry/2022/03/10/090000)

## Prerequisite

- Determining domains for GitLab Pages:
    - GitLab: `gitlab.training.com`
    - Pages: `pages.training.com`
- Making Wildcard DNS Record / Editing hosts
    - ***You need to edit /etc/hosts***
- Runner
- (Option) Certification for HTTPS

## Note

> You need to wait for accessing the gitlab (`http://gitlab.training.com`), because gitlab container initially do setup for some time.

- Initial root passwd: `server/gitlab/config/initial_root_password`
- Editing `/etc/hosts`
    ```
    ...
    192.168.100.10 gitlab.training.com
    192.168.100.10 pages.training.com
    192.168.100.10 *.pages.training.com
    ```

## Issue

- Runner of GitLab CI don't start
    - [Check **Run untagged jobs** => `Indicates whether this runner can pick jobs without tags`](https://kyamisama.hatenablog.com/entry/2020/12/28/151328)
- Gitlab Runner Container occurs error in ci pipeline with docker executer
    - [You need to add `clone_url`, `network_mode` and `volumes` attributes to `/etc/gitlab-runner/config.toml`](https://qiita.com/miyah/items/fe4fa1971056b6efe36c#docker-executer-%E3%81%AE%E8%A8%AD%E5%AE%9A%E3%82%92%E8%BF%BD%E5%8A%A0)
