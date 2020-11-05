
import { DockPanel } from 'phosphor-dockpanel'

import VueWidget from './VueWidget.js'

import panel1 from './panel1.vue'
import panel2 from './panel2.vue'
import panel3 from './panel3.vue'
import panel4 from './panel4.vue'
import panel5 from './panel5.vue'
import panel6 from './panel6.vue'



const w1 = new VueWidget(panel1, {
  title: '1 (unclosable)',
  closable: false,
})
const w2 = new VueWidget(panel2, {
  title: '2 (unclosable)',
  closable: false,
})
const w3 = new VueWidget(panel3, {
  title: '3',
  closable: true,
})
const w4 = new VueWidget(panel4, {
  title: '4',
  closable: true,
})
const w5 = new VueWidget(panel5, {
  title: '5',
  closable: true,
})
const w6 = new VueWidget(panel6, {
  title: '6',
  closable: true,
})



const panel = new DockPanel()
panel.attach(document.querySelector('#app'))
window.onresize = () => { panel.update() }

panel.insertLeft(w1)
/**
 * w1
 */

panel.insertLeft(w2, w1)
/**
 * w2 | w1
 */

panel.insertBottom(w3, w1)
/**
 * w2 | w1
 *    | w3
 */

panel.insertBottom(w4)
/**
 * w2 | w1
 *    | w3
 * -------
 * w4
 */

panel.insertTabBefore(w5, w4)
/**
 * w2 | w1
 *    | w3
 * -------
 * [w5,w4]
 */


let cnt = 0
document.querySelector('#btn').onclick = (e) => {
  w6.title.text += `-${cnt}`
  cnt++
  panel.insertRight(w6)
}

