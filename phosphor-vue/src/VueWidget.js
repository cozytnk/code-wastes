import Vue from 'vue'
import { Widget } from 'phosphor-widget'
import './VueWidget.css'


// REF: https://phosphorjs.github.io/examples/dockpanel/

export default class VueWidget extends Widget {

  constructor(vueComponent, titleOptions) {
    console.assert(vueComponent)

    super()
    this.addClass('content') // おまじない
    this.addClass(this.constructor.name.toLowerCase()) // 'vuewidget'

    // set title options
    if (titleOptions) {
      this.title.text = titleOptions.title || 'VueWidget'
      this.title.closable = titleOptions.closable || false
    }

    // Vueコンポーネントを適用

    // NOTE: this.id, this.node にVueを紐付けると
    //       パネルのcloseや移動時にエラーとなるため
    //       Vue適用対象とする子DOMを追加
    const el = document.createElement('div')
    this.node.appendChild(el)
    setTimeout(() => {
      new Vue({
        //el: `#${el.id}`,
        el: el,
        render: h => h(vueComponent),
      })
    })

  }

  onAfterAttach(msg) {
  }

  onResize(msg) {
    //this._xxx.setSize(msg.width, msg.height)
  }
}
