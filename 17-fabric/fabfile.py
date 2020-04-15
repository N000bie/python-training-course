from fabric import task


@task
def check_os(c):
    out = c.run('lsb_release -a')
    if out.failed or 'Ubuntu' not in out.stdout:
        print(c.host, 'is not a ubuntu server')
    else:
        print(c.host, 'is a ubuntu server')


# execute remote command with
#   `fab --prompt-for-login-password -H user@host check-os`
