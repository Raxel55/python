path_to_passwd = '/etc/passwd'
path_to_group = '/etc/group'
path_to_output = 'output.txt'

file = open(path_to_passwd,'r')
passwd = file.readlines()
file.close()

file = open(path_to_group,'r')
group = file.readlines()
file.close()

# 1. bash - count users

shells = []
for i in range(len(passwd)):
	shells.append(passwd[i].split(':')[-1][:-1])
shellset = set(shells)
shells_str = ''
for shell in shellset:
	shells_str+='%s - %d ; ' % (shell,shells.count(shell))

file = open(path_to_output,'w')
file.write(shells_str+'\n')
file.close()

# 2. group - UIDs

groups = []
users = []
for line in group:
	groups.append(line.split(':')[2::-2])
for line in passwd:
	users.append(line.split(':')[2:4])
groups = dict(groups)
group_and_uid = {}
for u in users:
	if groups[u[1]] not in group_and_uid:
		group_and_uid[groups[u[1]]] = [u[0]]
	else:
		group_and_uid[groups[u[1]]].append(u[0])
group_and_uid_str = ''
for k,v in group_and_uid.items():
	group_and_uid_str+='%s:%s, '%(k,','.join(v))

file = open(path_to_output,'a')
file.write(group_and_uid_str+'\n')
