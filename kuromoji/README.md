

- https://github.com/takuyaa/kuromoji.js
- [【Node.js】kuromoji.js + mecab-ipadic-neologdで形態素解析して遊ぶ - Qiita](https://qiita.com/mabasasi/items/17b0bf735c38b4642682)


```javascript
// snippet1
kuromoji.builder({ dicPath: './dict' }).build((err, tokenizer) => {
  if (err) {
    console.log(err)
    return
  }
  const tokens = tokenizer.tokenize(`すもももももももものうち`)
  console.log(tokens)
  console.log(JSON.stringify(tokens, null, 4))
})

// snippet2
const buildTokenizer = option => {
  return new Promise((resolve, reject) => {
    kuromoji.builder(option).build((err, tokenizer) => {
      if (err) reject(err)
      else     resolve(tokenizer)
    })
  })
}
const tokenizer = await buildTokenizer({ dicPath: './dict' })
const tokens = tokenizer.tokenize(`すもももももももものうち`)
console.log(tokens)
console.log(JSON.stringify(tokens, null, 4))


/*
(7) [{…}, {…}, {…}, {…}, {…}, {…}, {…}]
[
  {
      "word_id": 415760,
      "word_type": "KNOWN",
      "word_position": 1,
      "surface_form": "すもも",
      "pos": "名詞",
      "pos_detail_1": "一般",
      "pos_detail_2": "*",
      "pos_detail_3": "*",
      "conjugated_type": "*",
      "conjugated_form": "*",
      "basic_form": "すもも",
      "reading": "スモモ",
      "pronunciation": "スモモ"
  },
  {
      "word_id": 93220,
      "word_type": "KNOWN",
      "word_position": 4,
      "surface_form": "も",
      "pos": "助詞",
      "pos_detail_1": "係助詞",
      "pos_detail_2": "*",
      "pos_detail_3": "*",
      "conjugated_type": "*",
      "conjugated_form": "*",
      "basic_form": "も",
      "reading": "モ",
      "pronunciation": "モ"
  },
  {
      "word_id": 1614710,
      "word_type": "KNOWN",
      "word_position": 5,
      "surface_form": "もも",
      "pos": "名詞",
      "pos_detail_1": "一般",
      "pos_detail_2": "*",
      "pos_detail_3": "*",
      "conjugated_type": "*",
      "conjugated_form": "*",
      "basic_form": "もも",
      "reading": "モモ",
      "pronunciation": "モモ"
  },
  {
      "word_id": 93220,
      "word_type": "KNOWN",
      "word_position": 7,
      "surface_form": "も",
      "pos": "助詞",
      "pos_detail_1": "係助詞",
      "pos_detail_2": "*",
      "pos_detail_3": "*",
      "conjugated_type": "*",
      "conjugated_form": "*",
      "basic_form": "も",
      "reading": "モ",
      "pronunciation": "モ"
  },
  {
      "word_id": 1614710,
      "word_type": "KNOWN",
      "word_position": 8,
      "surface_form": "もも",
      "pos": "名詞",
      "pos_detail_1": "一般",
      "pos_detail_2": "*",
      "pos_detail_3": "*",
      "conjugated_type": "*",
      "conjugated_form": "*",
      "basic_form": "もも",
      "reading": "モモ",
      "pronunciation": "モモ"
  },
  {
      "word_id": 93100,
      "word_type": "KNOWN",
      "word_position": 10,
      "surface_form": "の",
      "pos": "助詞",
      "pos_detail_1": "連体化",
      "pos_detail_2": "*",
      "pos_detail_3": "*",
      "conjugated_type": "*",
      "conjugated_form": "*",
      "basic_form": "の",
      "reading": "ノ",
      "pronunciation": "ノ"
  },
  {
      "word_id": 62510,
      "word_type": "KNOWN",
      "word_position": 11,
      "surface_form": "うち",
      "pos": "名詞",
      "pos_detail_1": "非自立",
      "pos_detail_2": "副詞可能",
      "pos_detail_3": "*",
      "conjugated_type": "*",
      "conjugated_form": "*",
      "basic_form": "うち",
      "reading": "ウチ",
      "pronunciation": "ウチ"
  }
]
 */

```