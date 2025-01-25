import { promisify } from 'util';
import redis from 'redis';

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  const value = await getAsync(schoolName);
  console.log(value);
};

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
