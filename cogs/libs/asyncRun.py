import asyncio

async def asyncRun(cmd):
	proc = await asyncio.create_subprocess_shell(
		cmd,
		stdout=asyncio.subprocess.PIPE,
		stderr=asyncio.subprocess.PIPE)

	stdout, stderr = await proc.communicate()

	if stdout:
		return stdout.decode()
	return stderr.decode()
