exports.handler = async (event) => {
    const num1 = event.num1;
    const num2 = event.num2;
    const result = num1 + num2;

    return {
        statusCode: 200,
        body: JSON.stringify({ result: result })
    };
};