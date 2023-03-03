function sample() {
    const x = 3;

    const url = "http://localhost:8000/sample";

    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ x: x })
    }

    fetch(url, params).then((response) => {
        console.log(response);
        // console.log(response.text().then(console.log))
    })
    .catch((error) => {
        console.log(error);
    });
}
