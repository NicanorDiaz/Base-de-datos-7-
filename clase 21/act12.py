import redis

client = redis.Redis(host = '172.17.0.1', port = 6379)

client.lpush('Directores', "Tarantino")
client.lpush('Directores', "Spielberg")
client.lpush('Directores', "Hitchcock")

while (client.llen('Directores')!= 0):print (client.lpop('Directores'))
