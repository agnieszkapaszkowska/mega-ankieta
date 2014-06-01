$.widget("iss.multipleselectWidget", $.iss.multipleWidget, {

    _addAnswerCell: function(index, questionIndex) {
        var selectTag = '<select name="' + this.options.name() + '_' + questionIndex
            + '_' + index + '">';
        for (var i = 0; i < this.answers.length; i++) {
            selectTag += '<option value="'
                + this.answers[i].id() + '" '
                + '>' + this.answers[i].text() + '</option>';
        }
        return selectTag + '</select>';
    },

    _getValue: function(i, j) {
        return this.element.find("select")[0].selectedIndex.value;
    },
    
    _checkValue: function(i, j) {
        return this.element.find("select")[0].selectedIndex != -1;


    }
});
