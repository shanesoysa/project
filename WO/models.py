# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllRecords(models.Model):
    w_o_number = models.TextField(db_column='W/O NUMBER', blank=True,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    builder_name = models.TextField(db_column='BUILDER NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_time = models.TextField(db_column='START TIME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part = models.TextField(db_column='PART', blank=True, null=True)  # Field name made lowercase.
    customer_field = models.TextField(db_column='CUSTOMER:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    finish_time_field = models.TextField(db_column='FINISH TIME:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tire_size_field = models.TextField(db_column='TIRE SIZE:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    builder_field = models.TextField(db_column='BUILDER #:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    machine_field = models.TextField(db_column='MACHINE:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    treatment_mil_field = models.TextField(db_column='TREATMENT MIL:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serial_number_field = models.TextField(db_column='SERIAL NUMBER:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rim_diameter_field = models.TextField(db_column='RIM DIAMETER:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    inches_rubber_field = models.TextField(db_column='INCHES RUBBER:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tread_design_field = models.TextField(db_column='TREAD DESIGN:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rim_weight_field = models.TextField(db_column='RIM WEIGHT:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rim_w_center_field = models.TextField(db_column='RIM W/CENTER:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    r850_fiber_rubber_weight_field = models.TextField(db_column='R850 FIBER:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    r850_fiber_actual_field = models.TextField(db_column='R850 FIBER:(ACTUAL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    r803_fiber_rubber_weight_field = models.TextField(db_column='R803 FIBER:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    r803_fiber_actual_field = models.TextField(db_column='R803 FIBER:(ACTUAL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_80_duro_3_rubber_weight_field = models.TextField(db_column='80 DURO 3%:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_80_duro_3_actual_field = models.TextField(db_column='80 DURO 3%:(ACTUAL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_80_duro_3_type_rubber_field = models.TextField(db_column='80 DURO 3%:(TYPE RUBBER)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_65_duro_24_rubber_weight_field = models.TextField(db_column='65 DURO 24%:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_65_duro_24_actual_field = models.TextField(db_column='65 DURO 24%:(ACTUAL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_65_duro_24_type_rubber_field = models.TextField(db_column='65 DURO 24%:(TYPE RUBBER)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    setco_45_duro_rubber_weight_field = models.TextField(db_column='SETCO 45 DURO:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    setco_45_duro_actual_field = models.TextField(db_column='SETCO 45 DURO:(ACTUAL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    setco_45_duro_type_rubber_field = models.TextField(db_column='SETCO 45 DURO:(TYPE RUBBER)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_65_duro_3_rubber_weight_field = models.TextField(db_column='65 DURO 3%:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_65_duro_3_actual_field = models.TextField(db_column='65 DURO 3%:(ACTUAL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_65_duro_3_type_rubber_field = models.TextField(db_column='65 DURO 3%:(TYPE RUBBER)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    build_weight_rubber_weight_field = models.TextField(db_column='BUILD WEIGHT:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    build_weight_actual_field = models.TextField(db_column='BUILD WEIGHT:(ACTUAL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flash = models.TextField(db_column='FLASH', blank=True, null=True)  # Field name made lowercase.
    autoclave = models.TextField(db_column='AUTOCLAVE', blank=True, null=True)  # Field name made lowercase.
    mold_number = models.TextField(db_column='MOLD NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mold_temp_field = models.TextField(db_column='MOLD TEMP:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cure_time = models.TextField(db_column='CURE TIME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'All records'


class Comments(models.Model):
    comment = models.TextField(db_column='Comment', blank=True,primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Comments'


class ItemMaster(models.Model):
    w_o_number = models.TextField(db_column='W/O Number', blank=True,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    part_field = models.TextField(db_column='PART#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tire_size_field = models.TextField(db_column='TIRE SIZE:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    inches_rubber_field = models.TextField(db_column='INCHES RUBBER:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rim_diameter_field = models.TextField(db_column='RIM DIAMETER:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tread_design_field = models.TextField(db_column='TREAD DESIGN:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    r850_fiber_rubber_weight_field = models.TextField(db_column='R850 FIBER:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    r803_fiber_rubber_weight_field = models.TextField(db_column='R803 FIBER:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fiber3 = models.TextField(db_column='FIBER3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    setco_45_duro_rubber_weight_field = models.TextField(db_column='SETCO 45 DURO:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    number_65_duro_24_rubber_weight_field = models.TextField(db_column='65 DURO 24%:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_65_duro_3_rubber_weight_field = models.TextField(db_column='65 DURO 3%:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_80_duro_3_rubber_weight_field = models.TextField(db_column='80 DURO 3%:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    build_weight_rubber_weight_field = models.TextField(db_column='BUILD WEIGHT:(RUBBER WEIGHT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    inch2 = models.TextField(db_column='INCH2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cure_time = models.TextField(db_column='CURE TIME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        db_table = 'Item Master'


class ProductionSchedule(models.Model):
    order_field = models.TextField(db_column='Order#', blank=True,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    item_number = models.TextField(db_column='Item Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    number_80 = models.IntegerField(db_column='80', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_65_24_field = models.TextField(db_column='65 24%', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_65_3_field = models.IntegerField(db_column='65 3%', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_85 = models.IntegerField(db_column='85', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_45 = models.TextField(db_column='45', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Production Schedule'


class Wolinktable(models.Model):
    wo_field = models.TextField(db_column='WO#', blank=True,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    part_field = models.TextField(db_column='Part#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    customer_field = models.TextField(db_column='CUSTOMER:', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    builders_name = models.TextField(db_column='Builders Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_time = models.TextField(db_column='Start Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_time = models.TextField(db_column='End Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    builder = models.TextField(db_column='Builder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'WOLinkTable'
