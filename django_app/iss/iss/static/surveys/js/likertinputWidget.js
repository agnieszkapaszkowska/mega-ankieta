$.widget("iss.likertinputWidget", $.iss.likertextraWidget, {
    
    _addExtraCell: function(index, row) {
        $('<td><input id="' + this.questions[index].id() + '"></td>').appendTo(row);
    },

    _getExtraValue: function(row) {
        var input = row.find('input');
        return $("#" + input.attr("name")).val();
    }

});
