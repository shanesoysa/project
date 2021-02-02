from django.shortcuts import render
from .models import ProductionSchedule,Comments,AllRecords
from django.views.generic import ListView
from django.views.generic import View
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.template import RequestContext
from django.http import JsonResponse
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'forms/form.html')


class Report(ListView):
    model = ProductionSchedule
    template_name = 'forms/productionReport.html'
    context_object_name = 'productions'


def productionSchedule(request):
    comments = Comments.objects.all()
    return render(request, 'forms/productionSchedule.html',{'comments': comments})


def addProduction(request):
    order = request.GET.get('order', None)
    item = request.GET.get('item', None)
    description = request.GET.get('description', None)
    qty = request.GET.get('qty', None)
    time = request.GET.get('time', None)
    num80 = request.GET.get('num80', None)
    num6524 = request.GET.get('num6524', None)
    num653 = request.GET.get('num653', None)
    num85 = request.GET.get('num85', None)
    num45 = request.GET.get('num45', None)
    comment = request.GET.get('comment', None)
    status = request.GET.get('status', None)
    didupdate = request.GET.get('didupdate', None)


    if didupdate=="1":
        with connection.cursor() as cursor:
            cursor.execute('UPDATE "main"."Production Schedule" SET "Item Number"=%s,"Description"=%s,"Qty"=%s,"Time"=%s,"80"=%s,"65 24%"=%s,"65 3%"=%s,"85"=%s,"45"=%s,"Comment"=%s,"Status"=%s WHERE "Order#" = %s',
             [item,description,qty,time,num80,num6524,num653,num85,num45,comment,status,order])

    else:
        obj = ProductionSchedule.objects.create(
        order_field = order,
        item_number =item,
        description = description,
        qty = qty,
        time =time,
        number_80 =num80,
        number_65_24_field = num6524,
        number_65_3_field =num653, 
        number_85 =num85,
        number_45 = num45,
        comment =comment, 
        status = status
        )

    data = {
        'id': 'success'
    }
    return JsonResponse(data)



def SearchSchedule(request):
    ordernum = request.GET.get('ordernum', None)
   
    schedule = ProductionSchedule.objects.raw('SELECT * FROM "Production Schedule" WHERE "Production Schedule"."Order#" LIKE %s limit 1',[ordernum])
    
    for obj in schedule:        
        data = {
            'order_field': obj.order_field,
            'item_number': obj.item_number,
            'description': obj.description,
            'qty': obj.qty,
            'time': obj.time,
            'number_80': obj.number_80,
            'number_65_24_field': obj.number_65_24_field,
            'number_65_3_field': obj.number_65_3_field,
            'number_85': obj.number_85,
            'number_45': obj.number_45,
            'comment': obj.comment,
            'status': obj.status,
        }
        return JsonResponse(data)

def SearchBuild(request):
    wonumber = request.GET.get('wonumber', None)
   
    objs = AllRecords.objects.raw('SELECT * FROM "All records" WHERE "All records"."W/O NUMBER" LIKE %s limit 1',[wonumber])
    
    for obj in objs:
        data = {
            'w_o_number': obj.w_o_number,
            'date' :obj.date,
            'builder_name' :obj.builder_name,
            'start_time' :obj.start_time,
            'part' :obj.part,
            'customer_field' :obj.customer_field ,
            'finish_time_field' :obj.finish_time_field ,
            'tire_size_field' :obj.tire_size_field ,
            'builder_field' :obj.builder_field ,
            'machine_field' :obj.machine_field ,
            'treatment_mil_field' :obj.treatment_mil_field,
            'serial_number_field' :obj.serial_number_field ,
            'rim_diameter_field' :obj.rim_diameter_field ,
            'inches_rubber_field' :obj.inches_rubber_field,
            'tread_design_field' :obj.tread_design_field,
            'rim_weight_field' : obj.rim_weight_field,
            'rim_w_center_field' : obj.rim_w_center_field,
            'r850_fiber_rubber_weight_field' :obj.r850_fiber_rubber_weight_field,
            'r850_fiber_actual_field' :obj.r850_fiber_actual_field,
            'r803_fiber_rubber_weight_field' : obj.r803_fiber_rubber_weight_field,
            'r803_fiber_actual_field' : obj.r803_fiber_actual_field,
            'number_80_duro_3_rubber_weight_field' :obj.number_80_duro_3_rubber_weight_field,
            'number_80_duro_3_actual_field' :obj.number_80_duro_3_actual_field,
            'number_80_duro_3_type_rubber_field' :obj.number_80_duro_3_type_rubber_field ,
            'number_65_duro_24_rubber_weight_field' :obj.number_65_duro_24_rubber_weight_field,
            'number_65_duro_24_actual_field' :obj.number_65_duro_24_actual_field,
            'number_65_duro_24_type_rubber_field' :obj.number_65_duro_24_type_rubber_field,
            'setco_45_duro_rubber_weight_field' :obj.setco_45_duro_rubber_weight_field,
            'setco_45_duro_actual_field' : obj.setco_45_duro_actual_field,
            'setco_45_duro_type_rubber_field' :obj.setco_45_duro_type_rubber_field,
            'number_65_duro_3_rubber_weight_field' : obj.number_65_duro_3_rubber_weight_field,
            'number_65_duro_3_actual_field' :obj.number_65_duro_3_actual_field,
            'number_65_duro_3_type_rubber_field' : obj.number_65_duro_3_type_rubber_field,
            'build_weight_rubber_weight_field' :obj.build_weight_rubber_weight_field,
            'build_weight_actual_field' :obj.build_weight_actual_field,
            'flash' :obj.flash ,
            'autoclave' :obj.autoclave,
            'mold_number' :obj.mold_number,
            'mold_temp_field' :obj.mold_temp_field,
            'cure_time' :obj.cure_time,
            'notes' :obj.notes
        }
        return JsonResponse(data)


def addProductionSchedule(request):
    dater = request.GET.get('date', None)
    wonumber = request.GET.get('wonumber', None)
    buildername = request.GET.get('buildername', None)
    parti = request.GET.get('part', None)
    starttime = request.GET.get('starttime', None)
    customer = request.GET.get('customer', None)
    finishtime = request.GET.get('finishtime', None)
    tiresize = request.GET.get('tiresize', None)
    builder = request.GET.get('builder', None)
    machine = request.GET.get('machine', None)
    mill = request.GET.get('mill', None)
    serialnumber = request.GET.get('serialnumber', None)
    rimdiameter = request.GET.get('rimdiameter', None)
    inchesrubber = request.GET.get('inchesrubber', None)
    treaddesign = request.GET.get('treaddesign', None)
    rimweight = request.GET.get('rimweight', None)
    rimcenter = request.GET.get('rimcenter', None)
    r850w = request.GET.get('r850w', None)
    r850a = request.GET.get('r850a', None)
    r803w = request.GET.get('r803w', None)
    r803a = request.GET.get('r803a', None)
    duro803w = request.GET.get('duro803w', None)
    duro803a = request.GET.get('duro803a', None)
    duro803t = request.GET.get('duro803t', None)
    duro6524w = request.GET.get('duro6524w', None)
    duro6524a = request.GET.get('duro6524a', None)
    duro6524t = request.GET.get('duro6524t', None)
    secto45w = request.GET.get('secto45w', None)
    secto45a = request.GET.get('secto45a', None)
    secto45t = request.GET.get('secto45t', None)
    duro653w = request.GET.get('duro653w', None)
    duro653a = request.GET.get('duro653a', None)
    duro653t = request.GET.get('duro653t', None)
    buildw = request.GET.get('buildw', None)
    builda = request.GET.get('builda', None)
    flash = request.GET.get('flash', None)
    autoclavee = request.GET.get('autoclave', None)
    moldnumber = request.GET.get('moldnumber', None)
    moldtemp = request.GET.get('moldtemp', None)
    curetime = request.GET.get('curetime', None)
    note = request.GET.get('note', None)
    didupdate=request.GET.get('didupdate', None)

    if didupdate=="1":
        with connection.cursor() as cursor:
            cursor.execute('UPDATE "main"."All records" SET "DATE"=%s, "BUILDER NAME"=%s, "START TIME"=%s, "PART"=%s, "CUSTOMER:"=%s, "FINISH TIME:"=%s, "TIRE SIZE:"=%s, "BUILDER #:"=%s, "MACHINE:"=%s, "TREATMENT MIL:"=%s, "SERIAL NUMBER:"=%s, "RIM DIAMETER:"=%s, "INCHES RUBBER:"=%s, "TREAD DESIGN:"=%s, "RIM WEIGHT:"=%s, "RIM W/CENTER:"=%s, "R850 FIBER:(RUBBER WEIGHT)"=%s, "R850 FIBER:(ACTUAL)"=%s, "R803 FIBER:(RUBBER WEIGHT)"=%s, "R803 FIBER:(ACTUAL)"=%s, "80 DURO 3%:(RUBBER WEIGHT)"=%s, "80 DURO 3%:(ACTUAL)"=%s, "80 DURO 3%:(TYPE RUBBER)"=%s, "65 DURO 24%:(RUBBER WEIGHT)"=%s, "65 DURO 24%:(ACTUAL)"=%s, "65 DURO 24%:(TYPE RUBBER)"=%s, "SETCO 45 DURO:(RUBBER WEIGHT)"=%s, "SETCO 45 DURO:(ACTUAL)"=%s, "SETCO 45 DURO:(TYPE RUBBER)"=%s, "65 DURO 3%:(RUBBER WEIGHT)"=%s, "65 DURO 3%:(ACTUAL)"=%s, "65 DURO 3%:(TYPE RUBBER)"=%s, "BUILD WEIGHT:(RUBBER WEIGHT)"=%s, "BUILD WEIGHT:(ACTUAL)"=%s, "FLASH"=%s, "AUTOCLAVE"=%s, "MOLD NUMBER"=%s, "MOLD TEMP:"=%s, "CURE TIME"=%s, "NOTES"=%s WHERE "W/O NUMBER"=%s',
            [dater,buildername,starttime,parti,customer,finishtime,tiresize,builder,machine,mill,serialnumber,rimdiameter,inchesrubber,treaddesign,rimweight,rimcenter,r850w,r850a,r803w,r803a,duro803w,duro803a,duro803t,duro6524w,duro6524a,duro6524t,secto45w,secto45a,secto45t,duro653w,duro653a,duro653t,buildw,builda,flash,autoclavee,moldnumber,moldtemp,curetime,note,wonumber])
    else:
        obj = AllRecords.objects.create(
        w_o_number =wonumber,
        date = dater,
        builder_name =buildername,
        start_time =starttime,
        part = parti,
        customer_field = customer,
        finish_time_field = finishtime,
        tire_size_field = tiresize,
        builder_field = builder,
        machine_field = machine,
        treatment_mil_field = mill,
        serial_number_field = serialnumber,
        rim_diameter_field = rimdiameter,
        inches_rubber_field =inchesrubber,
        tread_design_field = treaddesign,
        rim_weight_field = rimweight,
        rim_w_center_field = rimcenter,
        r850_fiber_rubber_weight_field =r850w,
        r850_fiber_actual_field =r850a,
        r803_fiber_rubber_weight_field = r803w,
        r803_fiber_actual_field = r803a,
        number_80_duro_3_rubber_weight_field =duro803w,
        number_80_duro_3_actual_field =duro803a,
        number_80_duro_3_type_rubber_field = duro803t,
        number_65_duro_24_rubber_weight_field =duro6524w,
        number_65_duro_24_actual_field =duro6524a,
        number_65_duro_24_type_rubber_field =duro6524t,
        setco_45_duro_rubber_weight_field =secto45w,
        setco_45_duro_actual_field = secto45a,
        setco_45_duro_type_rubber_field =secto45t,
        number_65_duro_3_rubber_weight_field = duro653w,
        number_65_duro_3_actual_field =duro653a,
        number_65_duro_3_type_rubber_field = duro653t,
        build_weight_rubber_weight_field =buildw,
        build_weight_actual_field =builda,
        flash = flash,
        autoclave =autoclavee,
        mold_number =moldnumber,
        mold_temp_field =moldtemp,
        cure_time =curetime,
        notes =note 
        )

    data = {
        'id': 'success'
    }
    return JsonResponse(data)
