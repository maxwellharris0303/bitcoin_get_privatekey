from ecpy.curves import Curve
from ecpy.keys import ECPublicKey, ECPrivateKey
from sha3 import keccak_256

private_key = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

cv = Curve.get_curve('secp256k1')
pv_key = ECPrivateKey(private_key, cv)
pu_key = pv_key.get_public_key()

# equivalent alternative for illustration:
# concat_x_y = bytes.fromhex(hex(pu_key.W.x)[2:] + hex(pu_key.W.y)[2:])

concat_x_y = pu_key.W.x.to_bytes(32, byteorder='big') + pu_key.W.y.to_bytes(32, byteorder='big')
eth_addr = '0x' + keccak_256(concat_x_y).digest()[-20:].hex()

print('private key: ', hex(private_key))
print('eth_address: ', eth_addr)