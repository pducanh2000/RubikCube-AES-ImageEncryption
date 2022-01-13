# <b> Image Encryption/Decryption based on Rubik Cube 's principle and AES </b>

<b> Our final project for Theory of Crytography class. </b>


Our Image Encryption/Decryption method based on:

- <i> Rubik Cube principle ([paper here](https://www.hindawi.com/journals/jece/2012/173931/)) </i>

- <i> AES ([Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)) </i> 

This is my implementation of 3 main parts:
- [Encryption](#encrypt) 
- [Decryption](#decrypt) 
- [Evaluation](#eval)
- [Result](#result)

<a name= encrypt></a>
## <u> <b> Encryption </u> </b>

![encrypt_flow]("images/encrypt_flow.PNG")

- Three channels of the image are splited before encrypting with Rubik cube algorithm. The key of the encryption is encrypted by AES. 

- After that, these encrypted channels are combined to generate the Encrypted Image.


<a name= decrypt></a>
## <u> <b> Decryption </u> </b>

![decrypt_flow]("images/decrypt_flow.PNG")

The flow of decryption is the inverse transformation which is described below:
- Split the encrypted image to 3 encrypted channels

- Get the original key from the AES decrypt function

- Decrypt 3 channels with the decrypted key

The Encrypted Image 
<a name= eval></a>
## <u> <b> Evaluation </u> </b>

I propose two measures to quantify the differ between the encrypted image and its original form:
- Number of pixels change rate (NPCR)
- The unified average changing intensity (UACI)
![eval_functions]("images/eval_functions.PNG")

<a name= result></a>
## <u> <b> Results </u> </b>

### Original Image and Encrypted Image
![ori_enc_img]("images/ori_enc_img.PNG")

### Histogram 
![histogram]("images/histogram.PNG")


