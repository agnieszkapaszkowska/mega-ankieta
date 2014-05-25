$.widget("iss.multipleinputWidget", $.iss.multipleWidget, {

    _addAnswerCell: function(index, questionIndex) {
        return '<input style="max-width:50px;" type="number" id ="' + this.options.name() + '_'
            + questionIndex + '_' + index + '">';
    },

    _getValue: function(i, j) {
        return $('#' + this.options.name() + '_' + i + '_' + j).val();
    },

    _checkValue: function(i, j) {
        return ($('#' + this.options.name() + '_' + i + '_' + j).val().length > 0);
    }
});
