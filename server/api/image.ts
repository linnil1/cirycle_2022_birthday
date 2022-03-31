export default async (req, res, next) => {
    const name = req.url.slice(1)
    const value = await cirycle_2022_birthday.get(name, {type: "arrayBuffer"});
    // const value = new Uint8Array([255, 216, 255, 224]).buffer
    res.setHeader('Content-Type', 'image/jpeg');
    res.end(Buffer.from(new Uint8Array(value)))
}
