const AWS = require('aws-sdk');
const s3 = new AWS.S3();

exports.handler = async (event) => {
    const bucketName = 'your-s3-bucket-name';
    const fileName = event.fileName;
    const fileContent = Buffer.from(event.fileContent, 'base64');
    const params = {
        Bucket: bucketName,
        Key: fileName,
        Body: fileContent,
        ContentType: event.contentType || 'application/octet-stream'
    };

    try {
        const data = await s3.putObject(params).promise();
        return {
            statusCode: 200,
            body: JSON.stringify({ message: 'File uploaded successfully!', data: data })
        };
    } catch (err) {
        return {
            statusCode: 500,
            body: JSON.stringify({ message: 'Error uploading file', error: err })
        };
    }
};
