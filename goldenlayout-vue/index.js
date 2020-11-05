
import Vue from 'vue'
import c1 from './comp1.vue'

var config = {
  content: [{
    type: 'row',
    isClosable: false,
    content: [
      {
        type: 'component',
        componentName: 'c1',
        //showPopoutIcon: false, // NOTE: ここで指定しても反映されない
        componentState: { label: 'A' }
      },
      {
        type: 'column',
        content: [
          {
            type: 'component',
            isClosable: false,
            componentName: 'testComponent',
            componentState: { label: 'B' },
          },
          {
            type: 'component',
            componentName: 'testComponent',
            componentState: { label: 'C' }
          }
        ]
      }
    ]
  }]
}

const layout = new GoldenLayout(config, '#exampleLayoutContainer')


layout.registerComponent( 'c1', function(container, state) {
  const el = document.createElement('div')
  container.getElement().append(el)
  new Vue({
    el: el,
    render: h => h(c1),
  })
  var layoutSettings = container.layoutManager.config.settings
  //layoutSettings.showMaximiseIcon = false
  // REF: https://github.com/golden-layout/golden-layout/issues/491
	layoutSettings.showPopoutIcon = false
})
layout.registerComponent( 'testComponent', function(container, state) {
  container.getElement().html( '<h2>' + state.label + '</h2>' )
})

layout.init()

// [Refresh Golden-Layout size at resize of a DIV container · Issue #371 · golden-layout/golden-layout](https://github.com/golden-layout/golden-layout/issues/371)
$(window).resize(() => {
  //layout.updateSize($(window).width(), $(window).height())
  layout.updateSize($('.main').width(), $('.main').height())
})