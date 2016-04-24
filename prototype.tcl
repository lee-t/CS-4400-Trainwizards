#############################################################################
# Generated by PAGE version 4.7
# in conjunction with Tcl version 8.6
#    Apr 22, 2016 01:37:33 PM


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #111111
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top36
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top36 {base} {
    if {$base == ""} {
        set base .top36
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 600x450+338+180
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1165 768
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel 1"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but37 \
        -activebackground {#d9d9d9} -background {#d9d9d9} \
        -foreground {#000000} -highlightcolor black -text Login 
    vTcl:DefineAlias "$top.but37" "logbutton" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent38 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$top.ent38" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent39 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$top.ent39" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab41 \
        -background {#d9d9d9} -foreground {#000000} -text Username 
    vTcl:DefineAlias "$top.lab41" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab42 \
        -background {#d9d9d9} -foreground {#000000} -text Password 
    vTcl:DefineAlias "$top.lab42" "Label2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but43 \
        -activebackground {#d9d9d9} -background {#d9d9d9} \
        -foreground {#000000} -highlightcolor black -text Register 
    vTcl:DefineAlias "$top.but43" "regbutton" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but37 \
        -in $top -x 180 -y 260 -anchor nw -bordermode ignore 
    place $top.ent38 \
        -in $top -x 290 -y 160 -anchor nw -bordermode ignore 
    place $top.ent39 \
        -in $top -x 270 -y 210 -anchor nw -bordermode ignore 
    place $top.lab41 \
        -in $top -x 170 -y 160 -anchor nw -bordermode ignore 
    place $top.lab42 \
        -in $top -x 190 -y 210 -anchor nw -bordermode ignore 
    place $top.but43 \
        -in $top -x 320 -y 260 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top36
