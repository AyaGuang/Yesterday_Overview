package com.cyc.mapper;

import com.cyc.poji.user;
import org.apache.ibatis.annotations.Param;

import javax.swing.plaf.multi.MultiSliderUI;
import java.util.List;
import java.util.Map;

public interface userMapper {
    List<user> selectAll();
    void addSalary();
    List<user> select_on_condition(user user);
    void add(user user);
    void update(user user);
    void delete_by_ids(int[] ids);
}
