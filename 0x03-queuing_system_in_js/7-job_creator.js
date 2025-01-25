import kue from 'kue';

// Create a queue instance
const queue = kue.createQueue();

// Function to create a job
function createNotificationJob(phoneNumber, message) {
  const job = queue.create('push_notification_code', {
    phoneNumber,
    message
  });

  job
    .save()
    .on('enqueue', () => {
      console.log(`Job ${job.id} enqueued`);
    })
    .on('complete', () => {
      console.log(`Job ${job.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Job ${job.id} failed: ${err.message}`);
    });
}

export { createNotificationJob };

