$.widget("iss.multipleinputWidget", $.iss.multipleWidget, {

    _addAnswerCell: function(index, questionIndex) {
        return '<input style="max-width:50px;" type="number" id ="' + this.options.name() + '_'
            + questionIndex + '_' + index + '">';
    },

    _getValue: function(i, j) {
        return $('#' + name + '_' + i + '_' + j).val();
    }
});
