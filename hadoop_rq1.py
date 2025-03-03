import csv
import numpy as np
from sklearn.metrics import roc_auc_score

perf_induce_commits = ["03a9343d5798384b66fbd21e1e028acaf55b00e9",
"5877f20f9c3f6f0afa505715e9a2ee312475af17",
"638801cce16fc1dc3259c541dc30a599faaddda1",
"42307e3c3abbfe0b83d9a2581deba327435b910f",
"7136e8c5582dc4061b566cb9f11a0d6a6d08bb93",
"892ade689f9bcce76daae8f66fc00a49bee8548e",
"850d679acb935a6a6b0e6cb6f69d998e99395468",
"3c18a53cbd2efabb2ad108d63a0b0b558424115f",
"7905788db94d560e6668af0d4bed22b326961aaf",
"8b281bce85474501868d68f8d5590a6086abb7b7",
"401db4fc65140979fe7665983e36905e886df971",
"793447f79924c97c2b562d5e41fa85adf19673fe",
"3d65dbe032e202361d613344ccc6d9c5f99ba395",
"6dea01f1ee5ea3bf6e146e1b68616c2f43ba4792",
"734d54c1a8950446e68098f62d8964e02ecc2890",
"3671a5e16fbddbe5a0516289ce98e1305e02291c",
"d06948002fb0cabf72cc0d46bf2fa67d45370f67",
"8caf537afabc70b0c74e0a29aea0cc2935ecb162",
"9b90e52f1ec22c18cd535af2a569defcef65b093",
"9d175853b0170683ad5f21d9bcdeaac49fe89e04",
"475c6b4978045d55d1ebcea69cc9a2f24355aca2",
"4a3161182905afaf450a60d02528161ed1f97471",
"b1c7654ee40b372ed777525a42981c7cf55b5c72",
"24315e7d374a1ddd4329b64350cf96fc9ab6f59c",
"015535dc0ad00c2ba357afb3d1e283e56ddda0d6",
"042699401ebe5186fa5556a79f8f9a206e5ebcd7",
"0af44ea8462437f8e7a8271b15a19677fd7f05a1",
"0ba8ff4b77db11fb68111f20fb077cffddd24f17",
"1000a2af04b24c123a3b08168f36b4e90420cab7",
"185e0c7b4c056b88f606362c71e4a22aae7076e0",
"27941a1811831e0f2144a2f463d807755cd850b2",
"2d4097840c29116e9b000c158ce841d27863ad6e",
"3085a604300ed76d06a0011bd5555e419897b6cd",
"31f117138a00794de4951ee8433e304d72b04094",
"3dd6395bb2448e5b178a51c864e3c9a3d12e8bc9",
"693169ef34f856a27dc09d90a45fb4ec5b66ed2c",
"6c5bbd7a42d1e8b4416fd8870fd60c67867b35c9",
"6ef3a9e746c52d91f1e5b4ac9f41627bd42674d7",
"71a81b6257c0000475ad62eb69292a20d45d269c",
"832ebd8cb63d91b4aa4bfed412b9799b3b9be4a7",
"869393643de23dcb010cc33091c8eb398de0fd6c",
"9297f980c2de8886ff970946a2513e6890cd5552",
"a196766ea07775f18ded69bd9e8d239f8cfd3ccc",
"c95b878abf313507666ea018f9e6033c4c166e10",
"cc71ad80e184fc6e5043729e8cfcf6a62ca3e71f",
"cdb292f44caff9763631d9e9bcd69c375a7cddea",
"d27d7fc72e279614212c1eae52a84675073e89fb",
"d3797f9f3cf502b7bfee3b64c641807b276c6faf",
"e5afac5896a1a88e152746598527d91f73cbb724",
"f2231cebcddc80f0b753c4a7cb45ee4040846951",
"f32e9fc8f7150f0e889c0774b3ad712af26fbd65",
"5f34402adae191232fe78e62990396ca07f314bb",
"2fd19b9674420e025af54a5bed12eb96478f8c48",
"c78e3a7cdd10c40454e9acb06986ba6d8573cb19",
"f413ee33df301659c4ca9024380c2354983dcc84",
"48b9d5fd2a96728b1118be217ca597c4098e99ca",
"0a152103f19a3e8e1b7f33aeb9dd115ba231d7b7",
"53358fe680a11c1b66a7f60733d11c1f4efe0232",
"d331762f24b3f22f609366740c9c4f449edc61ac",
"e54cc2931262bf49682a8323da9811976218c03b",
"352cbaa7a54a94bad2bed131d6a250c5b21a7701",
"754cb4e30fac1c5fe8d44626968c0ddbfe459335",
"945db55f2e6521d33d4f90bbb09179b0feba5e7a",
"0d781dd03b979d65de94978071b2faa55005b34a",
"34f113df5cff2cc330fb671296932b8227b11975",
"de3b4aac561258ad242a3c5ed1c919428893fd4c",
"f64cfeaf61ec65a465decdd8215f567d4e6677a9",
"834e91ee91d22d74866afbf6252107e969bf8370",
"b38643c9a8dd2c53024ae830b9565a550d0ec39c",
"4fa1afdb883dab8786d2fb5c72a195dd2e87d711",
"^5128a9a453d64bfe1ed978cf9ffed27985eeef3",
"1770bb942f9ebea38b6811ba0bc3cc249ef3ccbb",
"54fe17a607ecbf90145bfc5364b25f0a5aee98f4",
"96da4be11c4c0e56cf6f14fe66007c4db4e5e861",
"ccaf036662e22da14583942054898c99fa51dae5",
"dbd07f9e8c2824cdb04d44d07d27c2b56f68c1d5",
"e7380b4f9c4f29bf5f0c07b95ddba88b0ef3765d",
"dbecbe5dfe50f834fc3b8401709079e9470cc517",
"d4324eef14782d3cde6570ee910c45d8fdfce6ba",
"6ee6eb843013324788f30384d9d967ff8743a970",
"a690a215dba6180090214675393431a589c37f24",
"03d46dc571bc5b0f1b3c0cb5daa52e7ee324dd54",
"0c278b0f636a01c81aba9e46fe7658fcdfb0f33c",
"0fd646b967443f44c237c95f93e03cb0a6a57f8d",
"1195f844a9a74de6709ba7d8aaf70c21f27cd2b3",
"1c8d64f38a86b92f3c5a56105cd0cd51d8b8529b",
"47cca0cb6d1f4e5979d11d9a624b005e6e666f2f",
"4b149a1e7781a52c2979fa3d367e4bfb1c4ccfe7",
"78ab699fe93cafbaff8f496be53d26aff40a68b1",
"e52f67e3897a67a0b6d29e557a31cfa881738821",
"02340a24f211212b91dc7380c1e5b54ddb5e82eb",
"f131dba8a3d603a5d15c4f035ed3da75b4daf0dc",
"520a39ac2daf86c0d67fff1b67f5f8d63e65114c",
"0a6806ce8c946b26eceac7d16b467c54c453df84",
"75ead273bea8a7dad61c4f99c3a16cab2697c498",
"c04a7d974aa5ae2589d36f63c4ac45fb42cd1b80",
"d3d019c337ecc10e9c6bbefc3a97c6cd1f5283c3",
"d5ef72e8c1816676b6106b353d7ca7d328721dd5",
"fbd88f1062f3c4b208724d208e3f501eb196dfab",
"42f90ab885d9693fcc1e52f9637f7de4111110ae",
"d16b17b4d299b4d58f879a2a15708bacd0938685",
"005850b28feb2f7bb8c2844d11e3f9d21b45d754",
"0a55bd841ec0f2eb89a0383f4c589526e8b138d4",
"8410d862d3a72740f461ef91dddb5325955e1ca5",
"341888a0aa23f24458b4e6e34868794b9735c06a",
"a44ce3f14fd940601f984fbf7980aa6fdc8f23b7",
"91f120f743662c6e037e8f21b1792e81d58ac664",
"00fe1ed3a4b3ee35fe24be257ec36445d2f44d63",
"ae047655f4355288406cd5396fb4e3ea7c307b14",
"1543d0f5be6a02ad00e7a33e35d78af8516043e3",
"86c9862bec0248d671e657aa56094a2919b8ac14",
"8c0638471f8f1dd47667b2d6727d4d2d54e4b48c",
"3dce234ed945f2dd5506e820141891a7d9306196",
"8236130b2c61ab0ee9b8ed747ce8cf96af7f17aa",
"cf7fe583d14ebb16fc1b6e29dc2afbf67d24b9d1",
"b59206190e6f773fc223bcb81774a09715551367",
"d749cf65e1ab0e0daf5be86931507183f189e855",
"60bd765ac1b7d21189efc47058c00ff956a2dc86",
"95363bcc7dae28ba9ae2cd7ee9a258fcb58cd932",
"1ef64e64c05ae5318cd4cb47d03a0494d742fb7c",
"4a574e9a84f2e997038452b22f2ad2a2d42e8ac8",
"4df8ed63ed93f2542e4b48f521b0cc6624ab59c1",
"718ad9f6ee93d4145f2bb19b7582ce4e1174feaf",
"c3973e7080bf71b57ace4a6adf4bb43f3c5d35b5",
"e74d1f0435c2bcdfae2c26f6c340a5a487d20aa3",
"b56daff6a186599764b046248565918b894ec116",
"4228de94028f1e10ca59ce23e963e488fe566909",
"2217e2f8ff418b88eac6ad36cafe3a9795a11f40",
"81bc395deb3ba00567dc067d6ca71bacf9e3bc82",
"0da69c324dee9baab0f0b9700db1cc5b623f8421",
"feb90ffcca536e7deac50976b8a8774450fe089f",
"9da9f7d4d8f1dce210995a06863a8836c23d7c3a",
"bbfaf3c2712c9ba82b0f8423bdeb314bf505a692",
"1268cf5fbe4458fa75ad0662512d352f9e8d3470",
"b6c7de68bc850ee5fa144eb3ea8d304065dbf4ea",
"e59f6fad6a8849cfab6acbf012f338d9cc7dd63c",
"bd909ed9f2d853f614f04a50e2230a7932732776",
"daf3e4ef8bf73cbe4a799d51b4765809cd81089f",
"15b7076ad5f2ae92d231140b2f8cebc392a92c87",
"6c348c56918973fd988b110e79231324a8befe12",
"bff7c90a5686de106ca7a866982412c5dfa01632",
"76ec26de8099dc48ce3812c595b7ab857a600442",
"bf669b6d9f8ba165e30b8823218d625a49958925",
"981679e6d7650141fc8737c7e13b16d8b795b408",
"5262b7ba4d018562d4e7d60772af4ddc3d770a23",
"1831be8e737fd423a9f3d590767b944147e85641",
"4e4b3a8465a8433e78e015cb1ce7e0dc1ebeb523",
"7558dbbb481eab055e794beb3603bbe5671a4b4c",
"b0c51504c494847a5d0e98d212660297ed43ba56",
"ef1a619a4df3a612eb293a6e8e1e952eaef18eba",
"453926397182078c65a4428eb5de5a90d6af6448",
"c53420f58364b11fbda1dace7679d45534533382",
"0fefda645bca935b87b6bb8ca63e6f18340d59f5",
"a45017a5f17ec11814db7e206d1e80aaa4dd8d8f",
"90dd3a8148468ac37a3f2173ad8d45e38bfcb0c9",
"666667464ad773449cd76b567312495577b3214d",
"519e5a7dd2bd540105434ec3c8939b68f6c024f8",
"83fe34ac0896cee0918bbfad7bd51231e4aec39b",
"f2ea555ac6c06a3f2f6559731f48711fff05d3f1",
"31f8da22d0b8d2dcce5fbc8e45d832f40acf056f",
"05f5c0f631680cffc36a79550c351620615445db",
"30d56fdbb40d06c4e267d6c314c8c767a7adc6a3",
"444b2ea7afebf9f6c3d356154b71abfd0ea95b23",
"83be3ad44484bf8a24cb90de4b9c26ab59d226a8",
"e5003be907acef87c2770e3f2914953f62017b0e",
"189a63a719c63b67a1783a280bfc2f72dcb55277",
"2b66d9ec5bdaec7e6b278926fbb6f222c4e3afaa",
"424fd9494f144c035fdef8c533be51e2027ad8d9",
"56e4f6237ae8b1852e82b186e08db3934f79a9db",
"658097d6da1b1aac8e01db459f0c3b456e99652f",
"6b608aad7d52b524fa94955a538e8b3524d42d93",
"86358221fc85a7743052a0b4c1647353508bf308",
"d3170f9eba9bc5c38b5fa50c24e37ca2bd5636c2",
"e0d131f055ee126052ad4d0f7b0d192e6c730188",
"6772d07fdc0ad7d0cd1be851bf83ae0208abd391",
"7f2b1eadc1b0807ec1302a0c3488bf6e7a59bc76",
"c39ca541f498712133890961598bbff50d89d68b",
"ec06957941367930c855b5e05e6a84ba676fd46a",
"0101267d9d801eab4cb3b4df289c402ecb591685",
"3cc73773eb26f7469c99b25a76814d6fad0be28e",
"561abb9fee5f57f74c2b5868a065b818678622fa",
"c1462a67ff7bb632df50e1c52de971cced56c6a3",
"085b1e293ff53f7a86aa21406cfd4bfa0f3bf33b",
"67ed59348d638d56e6752ba2c71fdcd69567546d",
"cdec12d1b84d444e13bf997c817643ec24aaa832",
"058af60c56207907f2bedf76df4284e86d923e0c",
"1d37a8812160bb030244a1e6b1c753f962d8d2ed",
"e8fc81f9c812b0c167411de7f1789a9a433a0d57",
"7d04a96027ad75877b41b7cd8f67455dd13159d7",
"a64dd3d24bfcb9af21eb63869924f6482b147fd3",
"e0f4620cc7db3db4b781e6042ab7dd754af28f18",
"109e528ef5d8df07443373751266b4417acc981a",
"968425e9f7b850ff9c2ab8ca37a64c3fdbe77dbf",
"2bc0a4f299fbd8035e29f62ce9cd22e209a62805",
"58db263e93daf08280e6a586a10cebd6122cf72a",
"c3cf331dc91e2beef2afeed11105084843b02858",
"083b44c136ea5aba660fcd1dddbb2d21513b4456",
"a3990ca41415515b986a41dacefceee1f05622f8",
"4709160d75a762ff1e189f49e28e84d59c3e8fd6",
"644548f201743408904dfe24b9f5b515b2c96713",
"e09ea0c06ee1caa5a9ebae0a8f0273dfe04d05e5",
"24d920b80eb3626073925a1d0b6dcf148add8cc0",
"27c4e90efce04e1b1302f668b5eb22412e00d033",
"29ae25801380b94442253c4202dee782dc4713f5",
"39ec1515a205952eda7e171408a8b83eceb4abde",
"c58a59f7081d55dd2108545ebf9ee48cf43ca944",
"b20180ffa6c89396d9fcfec8b029b9c600503c3d",
"95986dd2fb4527c43fa4c088c61fb7b4bd794d23",
"9c2848e076a5c72bda3ec928de1790137c70fbbc",
"5e09ae1633fb7fcf293ea10e663064e566c70909",
"dbf30e3c0e1522e6588aecac71c990c0b01fd8fb",
"71c8d735f5038e3b516947f12180d7568b6979dc",
"1035138b4c03ed26ce5be9fc4dd6f6c1e0af909b",
"2214871d916fdcae62aa51afbb5fd571f2808745",
"2860eeb14a958a8861b9ad3d6bd685df48da8cd3",
"3ab3a6498812c9fa0c53dae02ce696033062af87",
"782191f1ba27e0ff0acf3c6cf8a88df00274d308",
"8ab69eb0c3735d803b16472cea7a93bad9242573",
"0d91576ec31f63402f2db6107a04155368e2632d",
"0e76f1fceaaaeb66bdb4818f43b9a55fc092bf79",
"3ce0a6502e78240f551c29bb27a2324ce359cd70",
"460e98f7b3ec84f3c5afcb2aad4f4e7031d16e3a",
"5f6edb30c2bb648d5564c951edc25645e17e6636",
"8bc93db2e7c64830b6a662f28c8917a9eef4e7c9",
"235502d60b06d56a95edceecbf6f5b078a77d838",
"2a0147f8f698f22e61281c06691107e24a2f139c",
"a0f120ce68dddb0cb31b64c89f3224313f3cb5af",
"8ae98a9d1ca4725e28783370517cb3a3ecda7324",
"f26d2adbf98890cfe350c17241f5049b89a11e3c",
"6ae2a0d048e133b43249c248a75a4d77d9abb80d",
"daacbc18d739d030822df0b75205eeb067f89850",
"3343494d6c39883485d29c7439831ab3c1c7248d",
"3cdc100369ce920701fdddae12d7f7247332b3f3",
"b7442bf92eb6e1ae64a0f9644ffc2eee4597aad5",
"cc42ccf02acca7b5a971fa5ca0986e075169fc8c",
"47df4697ba22becdab530c0695b9a2a100798f94",
"61ab0440f7eaff0f631cbae0378403912f88d7ad",
"b64242c0d2cabd225a8fb7d25fed449d252e4fa1",
"63c966a3fbeb675959fc4101e65de9f57aecd17d",
"7723b139d55fc2c3954939559cb4914046a0f81c",
"98a692fd6361365db4afb9523a5d83ee32774112",
"b7f4a3156c0f5c600816c469637237ba6c9b330c",
"3eb61be352589491117ac2781bb18f55988a8084",
"e8477759ac7df7f30d0f74d3689458075cae0d9f",
"49f6e3d35e0f89637ae9ea970f249c13bdc0fd49",
"5c7cb51775bd3d4a6e3e1bd501b3a8d747733fe3",
"763f073f41e3eaa9ecd11c6ec0b76234739272aa",
"a3a9d72e98a9cc0f94af7c832dd13c408856636d",
"e3c696551952941ae0e38afed0323b80e02168c0",
"3e6fce91a471b4a5099de109582e7c6417e8a822",
"838b06ac87339494cea706d4a97e7f5383bdc442",
"1b3b9e5c31c38388c1ce4208c65e8dd5f956da82",
"a100be685cc4521e9949589948219231aa5d2733",
"8d5929308998869933982bd425102c3a9488ee8f",
"1ba3f8971433cdbc3e43fd3605065d811dab5b16",
"390642acf35f3d599271617d30ba26c2f6406fc1",
"3ae38ec7dfa1aaf451cf889cec6cf862379af32a",
"5e8837dd6cc747b3259751930f2a9eed7163bcad",
"a9d515aed870535ea80500c6dac7612720774cda",
"a317bd7b02c37bd57743bfad59593ec12f53f4ed",
"d31a41c35927f02f2fb40d19380b5df4bb2b6d57",
"89cab1ba5f0671f8ef30dbe7432079c18362b434",
"9523648d57ebc71cf5c57f3f8c52c4a63265b61c",
"10732d515f62258309f98e4d7d23249f80b1847d",
"3114d4731dcca7cb6c16aaa7c7a6550b7dd7dccb",
"57cdf8626a32b8595a645b7551f46ab950db4789",
"82f3454f5ac1f1c457e668e2cee12b4dcc800ee1",
"f6a778c3725bcdaba1e1de43786af17dd44deb78",
"02653add98f34deedc27f4da2254d25e83e55b58",
"06022b8fdc40e50eaac63758246353058e8cfa6d",
"fe67e30bc2794e7ff073cf938ee80eba805d1e69",
"18a3dad44afd8061643fffc5bbe50fa66e47b72c",
"3d0708bdb0a75af3d87bbac9f6c4ffbcabab98ca",
"a34dafe325902164c04de0bf9d34eccdf6a2cd88",
"fb06c0083799fa5ca514447ba6b63ce564272805",
"6ab25dfcd9cedecd43c30039ace33d1c234a7b43",
"81df7b586a16f8226c7b01c139c1c70c060399c3",
"9eee97508f350ed4629abb04e7781514ffa04070",
"63d9f1596c92206cce3b72e3214d2fb5f6242b90",
"f8f5887209a7d8e53c0a77abef275cbcaf1f7a5b",
"8c5b23b5473e447384f818d69d907d5c35ed6d6a",
"a54ccc0bde296b256a72ee4a627bbd93258c55b6",
"43100e9c0e14bae32ee0ca9e76b90e79561b568c",
"a38a37c63417a3b19dcdf98251af196c9d7b8c31",
"ccdb978603696a91c4828a66aad27f585543b376",
"abf833a7b228fff2bca4f69cd9df99d532380038",
"2f341414dd4a052bee3907ff4a6db283a15f9d53",
"31c91706f7d17da006ef2d6c541f8dd092fae077",
"8860e352c394372e4eb3ebdf82ea899567f34e4e",
"2690d0db0e860a05b0e46c234a3f82a82178c6c7",
"2c494a843699b478039f41336cf47bd4c635eb76",
"9a3f147fdd5421460889b266ead3a2300323cda2",
"cde987996ae727154b5081bf0a76e10c7c236118",
"dd72ca35365b59fcfc5724d2c182ff77e013fc47",
"022f7b4a25c73b8c43985e8d1bac717b96373ac6",
"5dae97a584d30cef3e34141edfaca49c4ec57913",
"b6ceee9bf42eec15891f60a014bbfa47e03f563c",
"70cff9e2f0c8f78c1dc54a064182971bb2106795",
"8b465b4b8caed31ca9daeaae108f9a868a30a455",
"de928d566a119f0b7fa5f171719642cd86be0af7",
"3cc7a38a53c8ae27ef6b2397cddc5d14a378203a",
"bc99aaffe7b0ed13b1efc37b6a32cdbd344c2d75",
"de480d6c8945bd8b5b00e8657b7a72ce8dd9b6b5",
"e37ca221bf4e9ae5d5e667d8ca284df9fdb33199",
"5137b388fc9d4d716f780daf6d04292feeb9df96",
"ceea91c9cd8b2a18be13217894ccf1c17198de18",
"6338ce3ae8870548cac5abe2f685748b5efb13c1",
"28bac402953a4337deedf0472611f5775c7a74c9",
"b503b6a07d7210c94657131dcd97239012ecb313",
"440c3cd1050f2a871a73d44406c0013b6ff73f2e",
"1e346aa829519f8a2aa830e76d9856f914861805",
"52ccc6c6d539d0587c3fd9693709bd1f6e12619d",
"5beeb3016954a3ee0c1fb10a2083ffd540cd2c14",
"ef9e1ba76357f6aaa5489ba1d5ed40ffff40a2cc",
"fd7de4c4eb3906e8e8a2631599dec78ff021d6c0",
"6f699e8ea5d8a48c3daaf8dffa2292ce0524cfdb",
"905a127850d5e0cba85c2e075f989fa0f5cf129a",
"063e33a862f99ce93b8399924c35d39ccd880f01",
"4186121c08cb3d86f775d333c637459a4fb19d1b",
"6b343adfe880c7e9e2f441fd889cf16a8657c335",
"2e61ed306f1d525096a800f28546601ef585a832",
"bc4b1f48d3aba7f7a324ae76ab65a0920b1e609e",
"47a381e306877750b5a3ce5d76e0a5ff652ec188",
"f025652fdafae4d385d4174f48cb4246d07caa3b",
"168bf7b71d2e8fc54e316c0b7d739be9de9157a3",
"f95ec3f5bf12bee07c90943cff3b135e6a7e7a8b",
"28e6a4e44a3e920dcaf858f9a74a6358226b3a63",
"10dc6b09272dbf2022907681e134104e7d418021",
"fake"]

p_tp = 0
p_fn = 0
p_fp = 0
p_tn = 0
np_tp = 0
np_fp = 0
np_fn = 0
np_tn = 0

p_prediction = []
p_actual = []
np_prediction = []
np_actual = []


perf_instances = 0
non_perf_instances = 0

file = 'hadoop_final_results.csv'
with open(file) as csvfile:
    commits = csv.DictReader(csvfile, delimiter=',')
    perf_instances = perf_instances + 1
    p_prediction.append(float(0))
    p_actual.append(0)
    for commit in commits:
        # print(commit['commit_hash'])
        if str(commit['x'])=='':
            next
        elif commit['commit_hash'] == "fake":
            perf_instances = perf_instances + 1
            p_prediction.append(float(0))
            p_actual.append(0)
        elif commit['commit_hash'] in perf_induce_commits:
            perf_instances = perf_instances + 1
            p_prediction.append(float(commit['x']))
            p_actual.append(int(commit['contains_bug']))
            if (float(commit['x'])>0 and commit['contains_bug']=="1"):
                p_tp = p_tp + 1
            elif (float(commit['x'])>0 and commit['contains_bug']=="0"):
                p_fp = p_fp + 1
            elif (float(commit['x'])==0 and commit['contains_bug']=="1"):
                p_fn = p_fn + 1
            elif (float(commit['x'])==0 and commit['contains_bug']=="0"):
                p_tn = p_tn + 1
        else:
            non_perf_instances = non_perf_instances + 1
            np_prediction.append(float(commit['x']))
            np_actual.append(int(commit['contains_bug']))
            if (float(commit['x'])>0 and commit['contains_bug']=="1"):
                np_tp = np_tp + 1
            elif (float(commit['x'])>0 and commit['contains_bug']=="0"):
                np_fp = np_fp + 1
            elif (float(commit['x'])==0 and commit['contains_bug']=="1"):
                np_fn = np_fn + 1
            elif (float(commit['x'])==0 and commit['contains_bug']=="0"):
                np_tn = np_tn + 1

csvfile.close()

# print(str(p_fn),"perf instances")
# print(str(non_perf_instances),"non-perf instances")


# performance_recall = p_tp/(p_tp+p_fn)
# performance_precision = p_tp/(p_tp+p_fp)
# performance_f1 = 2/((1/performance_recall)+(1/performance_precision))

# print(str(performance_recall))
# print(str(performance_precision))
# print(str(performance_f1))
# p_y_true = np.array(p_actual)
# p_y_scores = np.array(p_prediction)

# try:
#     roc_auc_score(p_y_true, p_y_scores)
#     print(str(roc_auc_score(p_y_true, p_y_scores)))
# except ValueError:
#     pass

# non_perf_recall = np_tp/(np_tp+np_fn)
# non_perf_precision = np_tp/(np_tp+np_fp)
# non_performance_f1 = 2/((1/non_perf_recall)+(1/non_perf_precision))

# print(str(non_perf_recall))
# print(str(non_perf_precision))
# print(str(non_performance_f1))
# np_y_true = np.array(np_actual)
# np_y_scores = np.array(np_prediction)

# try:
#     roc_auc_score(np_y_true, np_y_scores)
#     print(str(roc_auc_score(np_y_true, np_y_scores)))
# except ValueError:
#     pass

print(str(p_fn),"perf instances")
print(str(non_perf_instances),"non-perf instances")


performance_recall = p_tp/(p_tp+p_fn)
performance_precision = p_tp/(p_tp+p_fp)
performance_f1 = 2/((1/performance_recall)+(1/performance_precision))

print(str(performance_recall))
print(str(performance_precision))
print(str(performance_f1))
p_y_true = np.array(p_actual)
p_y_scores = np.array(p_prediction)
try:
    roc_auc_score(p_y_true, p_y_scores)
    print(str(roc_auc_score(p_y_true, p_y_scores)))
except ValueError:
    pass
non_perf_recall = np_tp/(np_tp+np_fn)
non_perf_precision = np_tp/(np_tp+np_fp)
non_performance_f1 = 2/((1/non_perf_recall)+(1/non_perf_precision))

print(str(non_perf_recall))
print(str(non_perf_precision))
print(str(non_performance_f1))
np_y_true = np.array(np_actual)
np_y_scores = np.array(np_prediction)
print(str(roc_auc_score(np_y_true, np_y_scores)))

print(str(p_tp))
total = p_tp + p_fn
print(str(total))