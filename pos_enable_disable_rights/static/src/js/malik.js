odoo.define('pos_enable_disable_rights.PosModel', function(require){
"use strict";

    var screens = require('point_of_sale.screens');
    var session = require('web.session');
    var Model = require('web.DataModel');

////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    screens.NumpadWidget.include({


    start: function() {
        this._super();
        var self = this;
        var buttonss = document.getElementsByClassName('mode-button');

        new Model("res.users")
                 .query(["id", "name", "pos_disc_al", "pos_pri_al", "pos_refund_al"])
                 .filter([['id', '=', session.uid]])
                 .first()
                 .then(function (results){
                       ////////////////////////////////
                       for(var i = 0; i < buttonss.length; i++){

                        if(buttonss[i].getAttribute("data-mode") === 'discount' && results.pos_disc_al === false){
                          buttonss.item(i).className += " disabled";
                          }
                          else if(buttonss[i].getAttribute("data-mode") === 'price' && results.pos_pri_al === false){
                          buttonss.item(i).className += " disabled";
                          }
                      }
                      if(results.pos_refund_al === false){
                          self.$el.find('.numpad-minus').addClass('disabled');
                          }
                       ///////////////////////////////
                 });







    },

    });

});
