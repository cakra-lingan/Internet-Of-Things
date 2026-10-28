import asyncio
import argparse
from aiocoap import Context, Message, GET


async def main(url):
    protocol = await Context.create_client_context()
    try:
        request = Message(code=GET, uri=url)
        print(f"Mengirim CoAP GET ke {url}...", flush=True)
        try:
            response = await asyncio.wait_for(
                protocol.request(request).response,
                timeout=10,
            )
        except asyncio.TimeoutError:
            raise SystemExit(
                "Timeout: tidak ada respons CoAP dalam 10 detik. "
                "Periksa log serial ESP32 dan pastikan firmware terbaru sudah diunggah."
            )

        print(f"Respons CoAP: {response.code}")
        print(response.payload.decode("utf-8", errors="replace"))
    finally:
        await protocol.shutdown()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a CoAP GET request.")
    parser.add_argument(
        "url",
        help="CoAP resource URL, for example coap://localhost/temp",
    )
    args = parser.parse_args()
    asyncio.run(main(args.url))